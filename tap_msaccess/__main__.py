"""MSAccess entry point.

Copyright (c) 2026 Meltano.
"""

from __future__ import annotations

from tap_msaccess.tap import TapMSAccess

TapMSAccess.cli()
