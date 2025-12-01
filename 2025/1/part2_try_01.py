#!/usr/bin/env python3
# Made by ChatGPT - 2025-12-01
#
# Advent of Code 2023 - Day 1: Secret Entrance (Part Two)
#
# Method 0x434C49434B:
# Count the number of times ANY CLICK causes the dial to point at 0,
# not just the final position after each rotation.
#
# Dial:
# - Positions 0–99 inclusive
# - Wraps around (mod 100)
# - Starts at 50
#
# Input:
# - One rotation per line in input2.txt
# - Each rotation: 'L<number>' or 'R<number>'

from __future__ import annotations
import sys
from typing import Iterable, Tuple, List


def parse_rotations(lines: Iterable[str]) -> List[Tuple[str, int]]:
    """Parse lines like 'L68' or 'R14' into (direction, distance) tuples."""
    rotations: List[Tuple[str, int]] = []
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


def zero_hits_in_rotation(position: int, direction: str, distance: int) -> Tuple[int, int]:
    """
    For a single rotation, return (number_of_clicks_landing_on_zero, new_position).

    We count every click where the dial *lands* on 0 while moving one step at a time.
    Mathematically:

    - Right rotation (R): positions visited are (position + k) % 100 for k = 1..distance.
      We want solutions to (position + k) % 100 == 0.

    - Left rotation (L): positions visited are (position - k) % 100 for k = 1..distance.
      We want solutions to (position - k) % 100 == 0.

    We find the first k where it hits 0, then count how many such ks there are
    spaced every 100 clicks.
    """
    if distance <= 0:
        # No clicks, no movement
        new_position = position
        return 0, new_position

    if direction == "R":
        # position + k ≡ 0 (mod 100)  =>  k ≡ -position (mod 100)
        first_k = (-position) % 100
    elif direction == "L":
        # position - k ≡ 0 (mod 100)  =>  k ≡ position (mod 100)
        first_k = position % 100
    else:
        raise ValueError(f"Unexpected direction: {direction!r}")

    # We need k >= 1, so if first_k == 0, the first zero is actually after 100 steps.
    if first_k == 0:
        first_k = 100

    if first_k > distance:
        hits = 0
    else:
        # First hit at first_k, then every +100 clicks afterward
        hits = 1 + (distance - first_k) // 100

    # Compute the final position after the full rotation
    if direction == "R":
        new_position = (position + distance) % 100
    else:  # direction == "L"
        new_position = (position - distance) % 100

    return hits, new_position


def count_zero_clicks_all(rotations: Iterable[Tuple[str, int]], start: int = 50) -> int:
    """
    Apply all rotations and count how many *clicks* land on 0
    (method 0x434C49434B).
    """
    position = start
    total_hits = 0

    for direction, distance in rotations:
        hits, position = zero_hits_in_rotation(position, direction, distance)
        total_hits += hits

    return total_hits


def run_with_input_file(filename: str = "input2.txt") -> None:
    """Read rotations from input2.txt (by default) and print the Part Two password."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    rotations = parse_rotations(lines)
    password = count_zero_clicks_all(rotations)
    print(password)


def run_test_example() -> None:
    """
    Run the example from the problem statement for Part Two.

    Example rotations:
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

    The expected answer for method 0x434C49434B is 6.
    """
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
    result = count_zero_clicks_all(rotations)

    print("Test example result (Part Two):", result)
    assert result == 6, f"Expected 6, got {result}"
    print("Test passed! ✅")


if __name__ == "__main__":
    # Usage:
    #   python day01_part2.py          -> uses input2.txt
    #   python day01_part2.py test     -> runs built-in example test
    if len(sys.argv) > 1 and sys.argv[1].lower() == "test":
        run_test_example()
    else:
        run_with_input_file()
