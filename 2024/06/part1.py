"""
Made by ChatGPT
Date: 2024-12-06

Solution for Advent of Code 2023 - Day 6: Guard Gallivant
"""

import sys
import argparse

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

def simulate_guard_path(grid):
    """
    Simulate the guard's path on the map and return the number of distinct positions visited.
    """
    rows, cols = len(grid), len(grid[0])
    r, c, direction = find_guard(grid)
    visited = set()
    visited.add((r, c))  # Include the starting position

    while 0 <= r < rows and 0 <= c < cols:
        # Determine the next position based on the current direction
        dr, dc = MOVES[direction]
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '#':
            # Turn right 90 degrees if there's an obstacle
            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
        else:
            # Move forward if there's no obstacle
            r, c = nr, nc
            if 0 <= r < rows and 0 <= c < cols:
                visited.add((r, c))
            else:
                break  # Guard has left the map

    return len(visited)

def main():
    parser = argparse.ArgumentParser(description="Solve Day 6: Guard Gallivant")
    parser.add_argument("-f", "--file", required=True, help="Input file containing the map")
    args = parser.parse_args()

    # Read the map from the input file
    grid = parse_map(args.file)

    # Simulate the guard's path
    visited_count = simulate_guard_path(grid)

    print(f"Number of distinct positions visited by the guard: {visited_count}")

if __name__ == "__main__":
    main()
