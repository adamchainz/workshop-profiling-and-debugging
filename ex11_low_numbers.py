from __future__ import annotations


def main() -> int:
    data = [5, 2, 12, 7, 3, 8]
    small = filter_small(data, 5)
    print(f"Found {len(small)} small numbers")  # Why is this always 0??
    return 0


def filter_small(numbers: list[int], bound: int) -> list[int]:
    for element in numbers:
        low = []
        if element < bound:
            low.append(element)
    return low


if __name__ == "__main__":
    raise SystemExit(main())
