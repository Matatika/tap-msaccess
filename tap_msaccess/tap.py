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
            description="Path to a Microsoft Access database `.mdb` or `.accdb` file",
        ),
    ).to_dict()

    @cached_property
    def db(self) -> AccessParser:
        """Database file parser."""
        config = {**self.config}
        database_file = config.pop("database_file")

        return AccessParser(fsspec.open(database_file, **config))

    def discover_streams(self) -> list[MSAccessStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [self._get_stream(table_name) for table_name in self.db.catalog]

    def _get_stream(self, table_name: str) -> MSAccessStream:
        table = self.db.parse_table_obj(table_name)
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
