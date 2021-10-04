from __future__ import annotations

import functools
import time
from collections.abc import Callable
from typing import Any, TypeVar, cast

# Our mini-profiler

Func = TypeVar("Func", bound=Callable[..., Any])


def instrument(func: Func) -> Func:  # decorator
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)

        # TODO: also print the duration by comparing start and end times
        print(f"{func.__name__}()")

        return result

    return cast(Func, wrapper)


time.sleep = instrument(time.sleep)  # monkey patch


# Our app


@instrument
def main() -> None:
    log("Starting main()")
    pause(0.25)
    log("Doing maths")
    sum(range(100_000))
    log("Final operation")
    pause(0.5)


def log(message: str) -> None:
    # Imagine this sends the message to our logging system.
    pass


def pause(n: float) -> None:
    time.sleep(n)


if __name__ == "__main__":
    main()
