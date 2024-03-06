"""Tests tap dynamic discovery."""

from itertools import zip_longest

import singer_sdk.typing as th
from singer_sdk.testing.templates import TapTestTemplate


class TapDynamicDiscoveryTest(TapTestTemplate):
    name = "dynamic_discovery"

    def test(self):
        streams = iter(self.tap.discover_streams())
        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysObjects"
        assert stream.primary_keys == ["Id"]

        self._assert_schema_properties(
            stream.schema,
            th.Property("Connect", th.StringType),
            th.Property("Database", th.StringType),
            th.Property("DateCreate", th.DateTimeType),
            th.Property("DateUpdate", th.DateTimeType),
            th.Property("Flags", th.IntegerType),
            th.Property("ForeignName", th.StringType),
            th.Property("Id", th.IntegerType),
            th.Property("Lv", th.StringType),
            th.Property("LvExtra", th.StringType),
            th.Property("LvModule", th.StringType),
            th.Property("LvProp", th.StringType),
            th.Property("Name", th.StringType),
            th.Property("Owner", th.StringType),
            th.Property("ParentId", th.IntegerType),
            th.Property("RmtInfoLong", th.StringType),
            th.Property("RmtInfoShort", th.StringType),
            th.Property("Type", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysComplexType_UnsignedByte"
        assert not stream.primary_keys

        self._assert_schema_properties(
            stream.schema,
            th.Property("Value", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysComplexType_Short"
        assert not stream.primary_keys

        self._assert_schema_properties(
            stream.schema,
            th.Property("Value", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysComplexType_Long"
        assert not stream.primary_keys

        self._assert_schema_properties(
            stream.schema,
            th.Property("Value", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysComplexType_IEEESingle"
        assert not stream.primary_keys

        self._assert_schema_properties(
            stream.schema,
            th.Property("Value", th.NumberType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysComplexType_IEEEDouble"
        assert not stream.primary_keys

        self._assert_schema_properties(
            stream.schema,
            th.Property("Value", th.NumberType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysComplexType_GUID"
        assert not stream.primary_keys

        self._assert_schema_properties(
            stream.schema,
            th.Property("Value", th.StringType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysComplexType_Decimal"
        assert not stream.primary_keys

        self._assert_schema_properties(
            stream.schema,
            th.Property("Value", th.StringType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysComplexType_Text"
        assert not stream.primary_keys

        self._assert_schema_properties(
            stream.schema,
            th.Property("Value", th.StringType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysComplexType_Attachment"
        assert not stream.primary_keys

        self._assert_schema_properties(
            stream.schema,
            th.Property("FileData", th.StringType),
            th.Property("FileFlags", th.IntegerType),
            th.Property("FileName", th.StringType),
            th.Property("FileTimeStamp", th.DateTimeType),
            th.Property("FileType", th.StringType),
            th.Property("FileURL", th.StringType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "Authors"
        assert stream.primary_keys == ["Au_ID"]

        self._assert_schema_properties(
            stream.schema,
            th.Property("Au_ID", th.IntegerType),
            th.Property("Author", th.StringType),
            th.Property("Year_Born", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysAccessStorage"
        assert stream.primary_keys == ["Id"]

        self._assert_schema_properties(
            stream.schema,
            th.Property("DateCreate", th.DateTimeType),
            th.Property("DateUpdate", th.DateTimeType),
            th.Property("Id", th.IntegerType),
            th.Property("Lv", th.StringType),
            th.Property("Name", th.StringType),
            th.Property("ParentId", th.IntegerType),
            th.Property("Type", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysNavPaneGroupCategories"
        assert stream.primary_keys == ["Id"]

        self._assert_schema_properties(
            stream.schema,
            th.Property("Filter", th.StringType),
            th.Property("Flags", th.IntegerType),
            th.Property("Id", th.IntegerType),
            th.Property("Name", th.StringType),
            th.Property("Position", th.IntegerType),
            th.Property("SelectedObjectID", th.IntegerType),
            th.Property("Type", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysNavPaneGroups"
        assert stream.primary_keys == ["Id"]

        self._assert_schema_properties(
            stream.schema,
            th.Property("Flags", th.IntegerType),
            th.Property("GroupCategoryID", th.IntegerType),
            th.Property("Id", th.IntegerType),
            th.Property("Name", th.StringType),
            th.Property("Object_Type_Group", th.IntegerType),
            th.Property("ObjectID", th.IntegerType),
            th.Property("Position", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysNavPaneGroupToObjects"
        assert stream.primary_keys == ["Id"]

        self._assert_schema_properties(
            stream.schema,
            th.Property("Flags", th.IntegerType),
            th.Property("GroupID", th.IntegerType),
            th.Property("Icon", th.IntegerType),
            th.Property("Id", th.IntegerType),
            th.Property("Name", th.StringType),
            th.Property("ObjectID", th.IntegerType),
            th.Property("Position", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "MSysNavPaneObjectIDs"
        assert not stream.primary_keys

        self._assert_schema_properties(
            stream.schema,
            th.Property("Id", th.IntegerType),
            th.Property("Name", th.StringType),
            th.Property("Type", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "Publishers"
        assert stream.primary_keys == ["PubID"]

        self._assert_schema_properties(
            stream.schema,
            th.Property("PubID", th.IntegerType),
            th.Property("Name", th.StringType),
            th.Property("Company_Name", th.StringType),
            th.Property("Address", th.StringType),
            th.Property("City", th.StringType),
            th.Property("State", th.StringType),
            th.Property("Zip", th.StringType),
            th.Property("Telephone", th.StringType),
            th.Property("Fax", th.StringType),
            th.Property("Comments", th.StringType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "Title_Author"
        assert stream.primary_keys == ["ISBN", "Au_ID"]

        self._assert_schema_properties(
            stream.schema,
            th.Property("ISBN", th.StringType),
            th.Property("Au_ID", th.IntegerType),
        )

        stream = next(streams, None)

        assert stream
        assert stream.name == "Titles"
        assert stream.primary_keys == ["ISBN"]

        self._assert_schema_properties(
            stream.schema,
            th.Property("Title", th.StringType),
            th.Property("Year_Published", th.IntegerType),
            th.Property("ISBN", th.StringType),
            th.Property("PubID", th.IntegerType),
            th.Property("Description", th.StringType),
            th.Property("Notes", th.StringType),
            th.Property("Subject", th.StringType),
            th.Property("Comments", th.StringType),
        )

        stream = next(streams, None)

        assert not stream

    def _assert_schema_properties(
        self,
        schema: dict,
        *expected_properties: th.Property,
    ) -> None:
        actual_properties: dict = schema["properties"]

        for actual, expected in zip_longest(
            ({k: v} for k, v in actual_properties.items()),
            (p.to_dict() for p in expected_properties),
        ):
            assert actual == expected
