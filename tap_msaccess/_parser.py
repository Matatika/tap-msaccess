"""MSAccess database file parser."""

import access_parser.utils as access_parser_utils
from access_parser import access_parser
from fsspec.core import OpenFile


class AccessParser(access_parser.AccessParser):
    def __init__(self, db_file: OpenFile) -> None:
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
