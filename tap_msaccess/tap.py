"""MSAccess tap class."""

from __future__ import annotations

from functools import cached_property

import access_parser.utils
from access_parser import AccessParser
from access_parser.access_parser import AccessTable, TableObj
from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_msaccess import utils
from tap_msaccess.client import MSAccessStream


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
        return AccessParser(self.config["database_file"])

    def discover_streams(self) -> list[MSAccessStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [self._get_stream(table_name) for table_name in self.db.catalog]

    def _get_stream(self, table_name: str) -> MSAccessStream:
        table = self._parse_table(table_name)
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

    def _parse_table(self, table_name: str) -> AccessTable:
        table_offset = self.db.catalog.get(table_name)

        if not table_offset:
            msg = f"Could not find table '{table_name}' in database"
            raise ValueError(msg)

        table_offset = table_offset * self.db.page_size
        table = self.db._tables_with_data.get(table_offset)  # noqa: SLF001

        if not table:
            table_def = self.db._table_defs.get(table_offset)  # noqa: SLF001
            if not table_def:
                msg = f"Could not find table '{table_name}' with offset '{table_offset}' in database"  # noqa: E501
                raise ValueError(msg)

            table = TableObj(offset=table_offset, val=table_def)
            self.logger.warning("Table '%s' has no data", table_name)

        props = (
            self.db.extra_props[table_name]
            if table_name != "MSysObjects" and table_name in self.db.extra_props
            else None
        )

        return AccessTable(
            table,
            self.db.version,
            self.db.page_size,
            self.db._data_pages,  # noqa: SLF001
            self.db._table_defs,  # noqa: SLF001
            props,
        )


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
