"""
Made by ChatGPT (ElfOffTheShelf)
Date: 2025-12-06

Advent of Code 2024 - Day 6 (Part Two)
--------------------------------------
Cephalopod math is written column-wise, right-to-left.

Rules:
 - Each *problem* is a horizontal block of columns, separated by blank columns.
 - Operator (+ or *) is on the *bottom* row of the problem block.
 - All rows above operator contain digits, but numbers are written:
       * One digit per column
       * Top digit = most significant
       * Bottom digit (just above operator row) = least significant
 - Read each column as one complete number.
 - Problems are evaluated right-to-left.

Two modes:
 - Test mode (example input)
 - Normal mode (reads input.txt)
"""

from pathlib import Path

TEST_MODE = False

TEST_INPUT = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

def read_input():
    if TEST_MODE:
        return TEST_INPUT.splitlines()
    else:
        return Path("input.txt").read_text().splitlines()

def parse_problems(lines):
    # Normalize to rectangle
    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    # Find column blocks (as before)
    problems = []
    current = []

    for col in range(width):
        blank = all(grid[r][col] == " " for r in range(len(grid)))
        if blank:
            if current:
                problems.append(current)
                current = []
        else:
            current.append(col)

    if current:
        problems.append(current)

    # Parse each problem RIGHT-to-left
    values = []

    for cols in problems:
        # Find operator in bottom row
        op_row = grid[-1]
        operator = None
        for c in cols:
            if op_row[c] in "+*":
                operator = op_row[c]
                break
        if operator is None:
            raise ValueError("No operator found in block.")

        # Build numbers column-by-column
        numbers = []
        # Each column is one whole number
        for c in cols:
            digits = []
            for r in range(len(grid) - 1):  # Exclude operator row
                ch = grid[r][c]
                if ch.isdigit():
                    digits.append(ch)
            if digits:
                num = int("".join(digits))
                numbers.append(num)

        # RIGHT-TO-LEFT: evaluation order is from last to first
        # But for + and * (commutative), order doesn't matter.
        # Still, we keep the concept.
        if operator == "+":
            value = sum(numbers)
        else:
            value = 1
            for n in numbers:
                value *= n

        values.append(value)

    return values

def main():
    lines = read_input()
    vals = parse_problems(lines)
    total = sum(vals)

    print("Problem values:", vals)
    print("Grand total:", total)

if __name__ == "__main__":
    main()
