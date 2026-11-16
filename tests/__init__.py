# Copyright (c) 2026 Meltano.

"""Test suite for tap-msaccess."""

from singer_sdk.testing.suites import SingerTestSuite

from tests.test_dynamic_discovery import TapDynamicDiscoveryTest

custom_tap_tests = SingerTestSuite(kind="tap", tests=[TapDynamicDiscoveryTest])
