from __future__ import annotations


def main() -> int:
    apple()
    return 0


def apple() -> None:
    year = 2001
    banana()
    print("In apple() the year is", year)


def banana() -> None:
    year = 2020
    cherry()
    print("In banana() the year is", year)


def cherry() -> None:
    year = 2021
    # breakpoint()
    print("In cherry() the year is", year)


if __name__ == "__main__":
    main()
