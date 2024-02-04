"""Test suite for tap-msaccess."""

from singer_sdk.testing.suites import TestSuite

from tests.test_dynamic_discovery import TapDynamicDiscoveryTest

custom_tap_tests = TestSuite(kind="tap", tests=[TapDynamicDiscoveryTest])
