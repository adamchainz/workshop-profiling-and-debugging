from __future__ import annotations

import random


def main() -> int:
    print(do_division())
    return 0


def do_division() -> int:
    return get_numerator() / get_denominator()


def get_numerator() -> int:
    return random.randint(0, 4)


def get_denominator() -> int:
    return 0


if __name__ == "__main__":
    main()
