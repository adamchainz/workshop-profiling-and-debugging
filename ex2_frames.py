from __future__ import annotations

import inspect
from types import FrameType


def apple() -> None:
    year = 2001  # noqa: F841
    banana()


def banana() -> None:
    year = 2020  # noqa: F841
    cherry()


def cherry() -> None:
    year = 2021  # noqa: F841
    frame: FrameType | None = inspect.currentframe()
    assert frame is not None
    print(f"Currently in: {frame.f_code.co_name}()")
    print(f"year = {frame.f_locals['year']}")

    # TODO: experiment interactively
    # breakpoint()

    # TODO: print value of 'year' in banana and apple.
    # Hint:
    # previous_frame = frame.f_back


if __name__ == "__main__":
    apple()
