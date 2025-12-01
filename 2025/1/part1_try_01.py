#!/usr/bin/env python3
# Made by ChatGPT - 2025-12-01
#
# Advent of Code 2023 - Day 1: Secret Entrance
#
# The dial has values 0–99, starts at 50, and we apply a sequence of rotations.
# After each rotation, if the dial points at 0, we increment our password counter.
# The answer is the total number of times the dial is at 0 after a rotation.

from __future__ import annotations
import sys
from typing import Iterable


def parse_rotations(lines: Iterable[str]) -> list[tuple[str, int]]:
    """Parse lines like 'L68' or 'R14' into (direction, distance) tuples."""
    rotations: list[tuple[str, int]] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        direction = line[0]
        if direction not in ("L", "R"):
            raise ValueError(f"Invalid direction in line: {line!r}")
        try:
            distance = int(line[1:])
        except ValueError as exc:
            raise ValueError(f"Invalid distance in line: {line!r}") from exc
        rotations.append((direction, distance))
    return rotations


def count_zero_hits(rotations: Iterable[tuple[str, int]], start: int = 50) -> int:
    """
    Apply rotations to the dial and count how many times it lands on 0.

    Dial has positions 0–99 inclusive and wraps around.
    """
    position = start
    zero_hits = 0

    for direction, distance in rotations:
        if direction == "R":
            position = (position + distance) % 100
        elif direction == "L":
            position = (position - distance) % 100
        else:
            # Should never happen if parsed correctly
            raise ValueError(f"Unexpected direction: {direction!r}")

        if position == 0:
            zero_hits += 1

    return zero_hits


def run_with_input_file(filename: str = "input.txt") -> None:
    """Read rotations from the given file and print the password."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    rotations = parse_rotations(lines)
    password = count_zero_hits(rotations)
    print(password)


def run_test_example() -> None:
    """Run the example from the problem statement and print debug info."""
    example_text = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
    rotations = parse_rotations(example_text.splitlines())
    result = count_zero_hits(rotations)

    print("Test example result:", result)
    assert result == 3, f"Expected 3, got {result}"
    print("Test passed! ✅")


if __name__ == "__main__":
    # Usage:
    #   python day01.py        -> uses input.txt
    #   python day01.py test   -> runs built-in example test
    if len(sys.argv) > 1 and sys.argv[1].lower() == "test":
        run_test_example()
    else:
        run_with_input_file()
