"""MSAccess database file parser."""

import access_parser.utils as access_parser_utils
from access_parser import access_parser
from fsspec.core import OpenFile


class AccessParser(access_parser.AccessParser):  # noqa: D101
    def __init__(self, db_file: OpenFile) -> None:  # noqa: D107
        with db_file.open() as f:
            self.db_data = f.read()

        self._parse_file_header(self.db_data)
        (
            self._table_defs,
            self._data_pages,
            self._all_pages,
        ) = access_parser_utils.categorize_pages(self.db_data, self.page_size)
        self._tables_with_data = self._link_tables_to_data()
        self.catalog = self._parse_catalog()
        self.extra_props = self.parse_msys_table()

    def parse_table_obj(  # noqa: D102
        self,
        table_name: str,
    ) -> access_parser.AccessTable:
        table_offset = self.catalog.get(table_name)

        if not table_offset:
            msg = f"Could not find table '{table_name}' in database"
            raise ValueError(msg)

        table_offset = table_offset * self.page_size
        table = self._tables_with_data.get(table_offset)

        if not table:
            table_def = self._table_defs.get(table_offset)
            if not table_def:
                msg = f"Could not find table '{table_name}' with offset '{table_offset}' in database"  # noqa: E501
                raise ValueError(msg)

            table = access_parser.TableObj(
                offset=table_offset,
                val=table_def,
            )
            access_parser.logging.warning("Table '%s' has no data", table_name)

        props = (
            self.extra_props[table_name]
            if table_name != "MSysObjects" and table_name in self.extra_props
            else None
        )

        return access_parser.AccessTable(
            table,
            self.version,
            self.page_size,
            self._data_pages,
            self._table_defs,
            props,
        )
