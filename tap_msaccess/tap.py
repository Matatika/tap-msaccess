"""MSAccess tap class."""

from __future__ import annotations

from functools import cached_property

import access_parser.utils
import fsspec
from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_msaccess import utils
from tap_msaccess.client import MSAccessStream
from tap_msaccess.parser import AccessParser


class TapMSAccess(Tap):
    """MSAccess tap class."""

    name = "tap-msaccess"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "database_file",
            th.StringType,
            required=True,
            description=(
                "Local or URL path to a Microsoft Access database `.mdb` or `.accdb` "
                "file"
            ),
        ),
        th.Property(
            "connection_params",
            th.ObjectType(additional_properties=True),
            description=(
                "Any parameters for the "
                "[`fsspec`](https://filesystem-spec.readthedocs.io/en/latest/) storage "
                "backend implementation dictated by the `database_file` URL protocol, "
                "such as "
                "[HTTP(S)](https://filesystem-spec.readthedocs.io/en/latest/api.html#fsspec.implementations.http.HTTPFileSystem)"
                ", "
                "[S3](https://s3fs.readthedocs.io/en/latest/) or "
                "[Azure](https://github.com/fsspec/adlfs?tab=readme-ov-file#readme) "
                "(see "
                "[built-in implementations](https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations)"
                " and "
                "[other known implementations](https://filesystem-spec.readthedocs.io/en/latest/api.html#other-known-implementations)"
                " for more information)"
            ),
        ),
    ).to_dict()

    @cached_property
    def db(self) -> AccessParser:
        """Database file parser."""
        config = {**self.config}
        database_file = config.pop("database_file")
        connection_params = config.pop("connection_params", {})

        return AccessParser(
            fsspec.open(
                database_file,
                **{
                    **config,
                    **connection_params,
                },
            )
        )

    def discover_streams(self) -> list[MSAccessStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [self._get_stream(table_name) for table_name in self.db.catalog]

    def _get_stream(self, table_name: str) -> MSAccessStream:
        table = self.db.get_table(table_name)
        properties = [
            th.Property(
                utils.sanitise_name(column["col_name_str"]),
                _parse_jsonschema_type(column["type"]),
            )
            for column in table.columns.values()
        ]

        schema = th.PropertiesList(*properties).to_dict()

        stream = MSAccessStream(self, schema, utils.sanitise_name(table_name))
        stream.table = table
        stream.primary_keys = table.primary_keys

        return stream


def _parse_jsonschema_type(type_id: int) -> th.JSONTypeHelper:
    if type_id is access_parser.utils.TYPE_BOOLEAN:
        return th.BooleanType

    if type_id in {
        access_parser.utils.TYPE_INT8,
        access_parser.utils.TYPE_INT16,
        access_parser.utils.TYPE_INT32,
    }:
        return th.IntegerType

    if type_id in {
        access_parser.utils.TYPE_FLOAT32,
        access_parser.utils.TYPE_FLOAT64,
    }:
        return th.NumberType

    if type_id is access_parser.utils.TYPE_DATETIME:
        return th.DateTimeType

    if type_id is access_parser.utils.TYPE_COMPLEX:
        return th.AnyType

    return th.StringType


if __name__ == "__main__":
    TapMSAccess.cli()
