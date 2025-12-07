"""
Made by ChatGPT — ElfOffTheShelf
Date: 2025-12-06

Advent of Code - Day 5: Cafeteria (Part 2)

This script reads a set of inclusive "fresh ingredient" ID ranges, merges any
overlapping ranges, and counts how many distinct ingredient IDs are included.
The available-ID section is ignored for Part 2.

Run normally to use 'input.txt', or run in test mode to verify logic using the
provided example.
"""

import sys

# ------------------------------------------------------------
# Example data for Test Mode (same ranges as Part 1)
# ------------------------------------------------------------
EXAMPLE_DATA = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def parse_ranges_only(text):
    """Parse only the ranges from the input; ignore the second section."""
    parts = text.strip().split("\n")

    # Find blank line index
    for i, line in enumerate(parts):
        if line.strip() == "":
            split_index = i
            break
    else:
        raise ValueError("Input missing blank line separator.")

    ranges = []
    for line in parts[:split_index]:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    return ranges


def merge_ranges(ranges):
    """
    Merge overlapping or touching ranges.
    Example:
        [(3,5), (4,8)] → [(3,8)]
    """
    if not ranges:
        return []

    # Sort by start
    ranges = sorted(ranges, key=lambda r: r[0])
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        # If overlapping or touching
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def count_total_ids(merged_ranges):
    """Count how many integers are covered across merged inclusive ranges."""
    total = 0
    for start, end in merged_ranges:
        total += (end - start + 1)
    return total


def main():
    test_mode = "--test" in sys.argv

    if test_mode:
        print("🎄 Running Part 2 in TEST MODE!")
        data = EXAMPLE_DATA
    else:
        with open("input.txt") as f:
            data = f.read()

    ranges = parse_ranges_only(data)
    merged = merge_ranges(ranges)
    total_fresh = count_total_ids(merged)

    print(f"Total fresh ingredient IDs: {total_fresh}")


if __name__ == "__main__":
    main()
