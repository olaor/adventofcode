# Made by ChatGPT on 2024-12-08

import argparse
from collections import defaultdict
from itertools import combinations

def parse_input(file_path):
    """Parse the map input from the file."""
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f]
    antennas = []
    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char != '.':
                antennas.append((x, y, char))
    return antennas, len(lines[0]), len(lines)

def find_antinode_positions(antennas, width, height):
    """
    Find all unique antinode positions in the map for Part Two.
    
    Args:
    - antennas: List of (x, y, frequency) tuples.
    - width: Width of the map.
    - height: Height of the map.
    
    Returns:
    - A set of unique antinode positions.
    """
    antinode_positions = set()
    frequency_map = defaultdict(list)

    # Group antennas by frequency
    for x, y, freq in antennas:
        frequency_map[freq].append((x, y))

    # Process each frequency group
    for freq, positions in frequency_map.items():
        # Add all antenna positions to the set of antinodes
        antinode_positions.update(positions)

        # Check combinations of pairs to determine collinear antinodes
        for (x1, y1), (x2, y2) in combinations(positions, 2):
            dx = x2 - x1
            dy = y2 - y1

            # Extend linearly in both directions
            k = 1
            while True:
                x_next, y_next = x1 - k * dx, y1 - k * dy
                if 0 <= x_next < width and 0 <= y_next < height:
                    antinode_positions.add((x_next, y_next))
                else:
                    break
                k += 1

            k = 1
            while True:
                x_next, y_next = x2 + k * dx, y2 + k * dy
                if 0 <= x_next < width and 0 <= y_next < height:
                    antinode_positions.add((x_next, y_next))
                else:
                    break
                k += 1

    return antinode_positions

def main():
    parser = argparse.ArgumentParser(description="Solve Day 8 Part Two: Resonant Collinearity.")
    parser.add_argument('-f', '--file', required=True, help="Path to the input file.")
    args = parser.parse_args()

    # Parse input file
    antennas, width, height = parse_input(args.file)

    # Find unique antinode positions
    antinodes = find_antinode_positions(antennas, width, height)

    # Output the result
    print(f"Number of unique locations containing an antinode: {len(antinodes)}")

if __name__ == "__main__":
    main()
