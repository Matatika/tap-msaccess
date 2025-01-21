"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_msaccess.tap import TapMSAccess
from tests import custom_tap_tests

SUITE_CONFIG = SuiteConfig(
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
    ],
)


# Run standard built-in tap tests from the SDK:
TestTapMSAccess = get_tap_test_class(
    tap_class=TapMSAccess,
    config={"database_file": "sample_db/Books.accdb"},
    custom_suites=[custom_tap_tests],
    suite_config=SUITE_CONFIG,
)

TestTapMSAccessS3 = get_tap_test_class(
    tap_class=TapMSAccess,
    config={
        "database_file": "s3://tap-msaccess/Books.accdb",
        "anon": True,
    },
    custom_suites=[custom_tap_tests],
    suite_config=SUITE_CONFIG,
)
