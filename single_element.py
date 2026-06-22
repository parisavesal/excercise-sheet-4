"""Find the only element that occurs exactly once in a list."""

from __future__ import annotations

import argparse
from collections import Counter


def find_single_element(values: list[int]) -> int:
    """Return the one integer that appears exactly once.

    All other integers must appear exactly twice. A ValueError is raised for
    inputs that do not follow this rule.
    """
    if not isinstance(values, list):
        raise TypeError("values must be a list")

    if len(values) % 2 == 0:
        raise ValueError("values must have an odd length")

    if not all(isinstance(value, int) for value in values):
        raise TypeError("all values must be integers")

    counts = Counter(values)
    singles = [value for value, count in counts.items() if count == 1]
    invalid_counts = [count for count in counts.values() if count not in (1, 2)]

    if len(singles) != 1 or invalid_counts:
        raise ValueError("exactly one element must occur once and all others twice")

    result = 0
    for value in values:
        result ^= value
    return result


def parse_args() -> argparse.Namespace:
    """Parse integer command-line input."""
    parser = argparse.ArgumentParser(description="Find the single element in a list.")
    parser.add_argument("values", nargs="+", type=int, help="Input integers")
    return parser.parse_args()


def main() -> None:
    """Run the method for command-line input."""
    args = parse_args()
    print(find_single_element(args.values))


if __name__ == "__main__":
    main()
