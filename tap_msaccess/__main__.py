# Copyright (c) 2026 Meltano.

"""MSAccess entry point."""

from __future__ import annotations

from tap_msaccess.tap import TapMSAccess

TapMSAccess.cli()
