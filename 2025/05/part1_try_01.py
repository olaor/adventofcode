"""
Made by ChatGPT — ElfOffTheShelf
Date: 2025-12-06

Advent of Code - Day 5: Cafeteria (Part 1)

This script reads a set of inclusive "fresh ingredient" ID ranges followed by a blank
line and then a list of available IDs. It counts how many of the available IDs fall
within *any* fresh range (ranges may overlap).

Run normally to use 'input.txt', or run in test mode to verify logic using the
provided example.
"""

import sys

# ------------------------------------------------------------
# Example data for Test Mode
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

def parse_input(text):
    """Parse the input into a list of ranges and available IDs."""
    parts = text.strip().split("\n")

    # Split at the blank line that separates ranges from available IDs
    ranges = []
    available = []

    # Find blank line index
    for i, line in enumerate(parts):
        if line.strip() == "":
            split_index = i
            break
    else:
        raise ValueError("Input missing blank line separator.")

    # Parse fresh ranges
    for line in parts[:split_index]:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    # Parse available IDs
    for line in parts[split_index + 1:]:
        available.append(int(line))

    return ranges, available


def is_fresh(ingredient_id, ranges):
    """Return True if ingredient_id falls inside ANY range."""
    return any(start <= ingredient_id <= end for start, end in ranges)


def count_fresh(ranges, available):
    """Count how many available IDs are fresh."""
    return sum(1 for x in available if is_fresh(x, ranges))


def main():
    test_mode = "--test" in sys.argv

    if test_mode:
        print("🎄 Running in TEST MODE!")
        data = EXAMPLE_DATA
    else:
        with open("input.txt") as f:
            data = f.read()

    ranges, available = parse_input(data)
    result = count_fresh(ranges, available)

    print(f"Fresh ingredient count: {result}")


if __name__ == "__main__":
    main()
