"""tap-msaccess utilities.

Copyright (c) 2026 Meltano.
"""

import re


def sanitise_name(name: str) -> str:  # noqa: D103
    return re.sub(r"\s+", "_", name.strip())
