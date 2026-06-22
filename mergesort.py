"""Merge sort example with a simple before/after visualization."""

from __future__ import annotations

import matplotlib.pyplot as plt


def merge_sort(values: list[int]) -> None:
    """Sort values in place using the merge sort algorithm.

    The function keeps the same behaviour as the original code: the input list is
    modified directly and nothing is returned.
    """
    if len(values) <= 1:
        return

    middle_index = len(values) // 2
    left_half = values[:middle_index]
    right_half = values[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)
    merge(values, left_half, right_half)


def merge(values: list[int], left_half: list[int], right_half: list[int]) -> None:
    """Merge two sorted lists into values."""
    left_index = 0
    right_index = 0
    merged_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            values[merged_index] = left_half[left_index]
            left_index += 1
        else:
            values[merged_index] = right_half[right_index]
            right_index += 1
        merged_index += 1

    while left_index < len(left_half):
        values[merged_index] = left_half[left_index]
        left_index += 1
        merged_index += 1

    while right_index < len(right_half):
        values[merged_index] = right_half[right_index]
        right_index += 1
        merged_index += 1


def plot_values(values: list[int], title: str) -> None:
    """Create a bar plot for the current list values."""
    indices = range(len(values))
    plt.figure(figsize=(8, 4))
    plt.bar(indices, values)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def main() -> None:
    """Run the merge sort example."""
    numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    plot_values(numbers, "Values before merge sort")
    merge_sort(numbers)
    plot_values(numbers, "Values after merge sort")


if __name__ == "__main__":
    main()
