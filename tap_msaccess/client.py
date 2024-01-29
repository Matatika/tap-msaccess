"""Custom client handling, including MSAccessStream base class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Iterable

from singer_sdk.streams import Stream

from tap_msaccess import utils

if TYPE_CHECKING:
    from access_parser.access_parser import AccessTable


class MSAccessStream(Stream):
    """Stream class for MSAccess streams."""

    table: AccessTable

    def get_records(  # noqa: D102
        self,
        context: dict | None,  # noqa: ARG002
    ) -> Iterable[dict]:
        table_data = self.table.parse()
        column_names = [utils.sanitise_name(name) for name in table_data]
        column_data = table_data.values()

        for data in zip(*column_data):
            yield {name: data[i] for i, name in enumerate(column_names)}
