"""
Made by ChatGPT (ElfOffTheShelf)
Date: 2025-12-06

Advent of Code 2024 - Day 6: Trash Compactor
--------------------------------------------
This script reads a horizontally-arranged worksheet where each *column-block*
represents a problem. Each problem consists of one operator row (*) or (+)
at the bottom and one or more number rows above it. Problems are separated by
a column of spaces.

Two modes:
 - TEST MODE: uses hardcoded example.
 - NORMAL MODE: reads from input.txt.

Run normally to process input.txt, or set TEST_MODE = True to run the example.
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
    # Normalize: ensure all lines have same length
    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    # A problem is a block of columns between blank columns
    problems = []
    current_cols = []

    col = 0
    while col < width:
        # Check whether this column is entirely spaces
        is_blank = all(row[col] == " " for row in grid)

        if is_blank:
            # End of a problem-block
            if current_cols:
                problems.append(current_cols)
                current_cols = []
        else:
            current_cols.append(col)
        col += 1

    # Add last block if present
    if current_cols:
        problems.append(current_cols)

    parsed = []

    # For each block of columns, extract numbers and operator
    for cols in problems:
        # Bottom row contains operator
        op_row = grid[-1]
        operator = None
        for c in cols:
            if op_row[c] in "+*":
                operator = op_row[c]
                break
        if operator is None:
            raise ValueError("Operator not found in problem block.")

        # All rows above bottom contain numbers (possibly right/left aligned)
        numbers = []
        for r in range(len(grid) - 1):
            row = grid[r]
            chunk = "".join(row[c] for c in cols).strip()
            if chunk:
                numbers.append(int(chunk))

        if operator == "+":
            value = sum(numbers)
        else:
            value = 1
            for n in numbers:
                value *= n

        parsed.append(value)

    return parsed

def main():
    lines = read_input()
    problem_values = parse_problems(lines)
    total = sum(problem_values)

    print("Individual problem values:", problem_values)
    print("Grand total:", total)

if __name__ == "__main__":
    main()
