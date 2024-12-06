#!/usr/bin/env python3
"""
Made by ChatGPT
Date: 2024-12-04
"""

import argparse

# Define all possible directions
DIRECTIONS = [
    (0, 1),   # Horizontal right
    (0, -1),  # Horizontal left
    (1, 0),   # Vertical down
    (-1, 0),  # Vertical up
    (1, 1),   # Diagonal down-right
    (-1, -1), # Diagonal up-left
    (1, -1),  # Diagonal down-left
    (-1, 1)   # Diagonal up-right
]

def read_grid(file_path):
    """Reads the grid from the specified file."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def in_bounds(x, y, rows, cols):
    """Checks if a position is within the grid bounds."""
    return 0 <= x < rows and 0 <= y < cols

def count_word(grid, word):
    """Counts occurrences of a word in all directions in the grid."""
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in DIRECTIONS:
                # Check if the word fits in the current direction
                if all(
                    in_bounds(r + dr * i, c + dc * i, rows, cols) and
                    grid[r + dr * i][c + dc * i] == word[i]
                    for i in range(word_len)
                ):
                    count += 1
    return count

def main():
    parser = argparse.ArgumentParser(description="Solve the Ceres Search puzzle.")
    parser.add_argument("-f", "--file", required=True, help="Input file containing the word search grid")
    args = parser.parse_args()
    
    # Read the grid from the input file
    grid = read_grid(args.file)
    
    # Count occurrences of the word "XMAS"
    total_count = count_word(grid, "XMAS")
    
    # Print the result
    print(f"Total occurrences of 'XMAS': {total_count}")

if __name__ == "__main__":
    main()

