"""
Made by ChatGPT
Date: 2024-12-06

Solution for Advent of Code 2023 - Day 6: Guard Gallivant (Part 2)
"""

import sys
import argparse
from copy import deepcopy

# Movement and direction helpers
DIRECTIONS = ['^', '>', 'v', '<']  # Up, Right, Down, Left
MOVES = {
    '^': (-1, 0),  # Move up
    '>': (0, 1),   # Move right
    'v': (1, 0),   # Move down
    '<': (0, -1)   # Move left
}

def parse_map(file_path):
    """Parse the map input file."""
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def find_guard(grid):
    """Locate the guard's initial position and facing direction."""
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in DIRECTIONS:
                return r, c, cell
    raise ValueError("Guard not found on the map!")

def simulate_guard_path(grid, r, c, direction):
    """
    Simulate the guard's path on the map and determine if a loop occurs.
    Returns True if a loop is detected, False otherwise.
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()
    state = (r, c, direction)

    while 0 <= r < rows and 0 <= c < cols:
        if state in visited:
            return True  # Loop detected
        visited.add(state)

        # Determine the next position based on the current direction
        dr, dc = MOVES[direction]
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '#':
            # Turn right 90 degrees if there's an obstacle
            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
        else:
            # Move forward if there's no obstacle
            r, c = nr, nc

        state = (r, c, direction)

    return False  # No loop detected

def find_loop_positions(grid):
    """
    Find all positions where adding an obstruction would cause the guard to get stuck in a loop.
    Returns a list of valid positions.
    """
    rows, cols = len(grid), len(grid[0])
    original_grid = deepcopy(grid)
    guard_r, guard_c, guard_dir = find_guard(grid)
    valid_positions = []

    for r in range(rows):
        for c in range(cols):
            # Skip the guard's starting position and existing obstructions
            if (r, c) == (guard_r, guard_c) or grid[r][c] == '#':
                continue

            # Temporarily place an obstruction
            grid[r][c] = '#'

            # Check if the guard gets stuck in a loop
            if simulate_guard_path(grid, guard_r, guard_c, guard_dir):
                valid_positions.append((r, c))

            # Remove the obstruction
            grid[r][c] = original_grid[r][c]

    return valid_positions

def main():
    parser = argparse.ArgumentParser(description="Solve Day 6: Guard Gallivant (Part 2)")
    parser.add_argument("-f", "--file", required=True, help="Input file containing the map")
    args = parser.parse_args()

    # Read the map from the input file
    grid = parse_map(args.file)

    # Find positions where a new obstruction causes the guard to get stuck in a loop
    valid_positions = find_loop_positions(grid)

    print(f"Number of valid positions for obstruction: {len(valid_positions)}")
    print("Valid positions:", valid_positions)

if __name__ == "__main__":
    main()
