"""tap-msaccess utilities."""

import re


def sanitise_name(name: str) -> str:  # noqa: D103
    return re.sub(r"\s+", "_", name.strip())
