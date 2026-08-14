"""Test suite for tap-msaccess.

Copyright (c) 2026 Meltano.
"""

from singer_sdk.testing.suites import TestSuite

from tests.test_dynamic_discovery import TapDynamicDiscoveryTest

custom_tap_tests = TestSuite(kind="tap", tests=[TapDynamicDiscoveryTest])
