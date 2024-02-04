"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_msaccess.tap import TapMSAccess

SAMPLE_CONFIG = {"database_file": "sample_db/Books.accdb"}

# Run standard built-in tap tests from the SDK:
TestTapMSAccess = get_tap_test_class(
    tap_class=TapMSAccess,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(
        ignore_no_records_for_streams=[
            "MSysComplexType_UnsignedByte",
            "MSysComplexType_Short",
            "MSysComplexType_Long",
            "MSysComplexType_IEEESingle",
            "MSysComplexType_IEEEDouble",
            "MSysComplexType_GUID",
            "MSysComplexType_Decimal",
            "MSysComplexType_Text",
            "MSysComplexType_Attachment",
        ]
    ),
)
