"""Custom client handling, including MSAccessStream base class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from singer_sdk.streams import Stream
from typing_extensions import override

from tap_msaccess import utils

if TYPE_CHECKING:
    from access_parser.access_parser import AccessTable


class MSAccessStream(Stream):
    """Stream class for MSAccess streams."""

    table: AccessTable

    @override
    def get_records(self, context):
        table_data = self.table.parse()
        column_names = [utils.sanitise_name(name) for name in table_data]
        column_data = table_data.values()

        for data in zip(*column_data):
            yield {name: data[i] for i, name in enumerate(column_names)}
