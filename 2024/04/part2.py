#!/usr/bin/env python3
"""
Made by ChatGPT
Date: 2024-12-04
"""

import argparse

# Define relative positions for the "X-MAS" pattern
DIAGONAL_1 = [(-1, -1), (0, 0), (1, 1)]  # Top-left to bottom-right
DIAGONAL_2 = [(-1, 1), (0, 0), (1, -1)]  # Top-right to bottom-left
VERTICAL = [(-1, 0), (0, 0), (1, 0)]     # Vertical

def read_grid(file_path):
    """Reads the grid from the specified file."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def in_bounds(x, y, rows, cols):
    """Checks if a position is within the grid bounds."""
    return 0 <= x < rows and 0 <= y < cols

def matches_pattern(grid, r, c, pattern, word):
    """Checks if a given pattern matches starting at a grid position."""
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    return all(
        in_bounds(r + dr, c + dc, rows, cols) and
        grid[r + dr][c + dc] == word[i]
        for i, (dr, dc) in enumerate(pattern)
    )

def count_xmas(grid):
    """Counts the number of X-MAS patterns in the grid."""
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            # Check for both diagonal and vertical patterns forming an "X-MAS"
            if (
                (matches_pattern(grid, r, c, DIAGONAL_1, "MAS") or
                 matches_pattern(grid, r, c, DIAGONAL_1[::-1], "MAS")) and
                (matches_pattern(grid, r, c, VERTICAL, "MAS") or
                 matches_pattern(grid, r, c, VERTICAL[::-1], "MAS"))
            ):
                count += 1
            if (
                (matches_pattern(grid, r, c, DIAGONAL_2, "MAS") or
                 matches_pattern(grid, r, c, DIAGONAL_2[::-1], "MAS")) and
                (matches_pattern(grid, r, c, VERTICAL, "MAS") or
                 matches_pattern(grid, r, c, VERTICAL[::-1], "MAS"))
            ):
                count += 1

    return count

def main():
    parser = argparse.ArgumentParser(description="Solve the X-MAS puzzle.")
    parser.add_argument("-f", "--file", required=True, help="Input file containing the word search grid")
    args = parser.parse_args()
    
    # Read the grid from the input file
    grid = read_grid(args.file)
    
    # Count occurrences of the X-MAS pattern
    total_count = count_xmas(grid)
    
    # Print the result
    print(f"Total X-MAS patterns found: {total_count}")

if __name__ == "__main__":
    main()
