# Made by ChatGPT on 2024-12-08

import argparse
from collections import defaultdict

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
    Find all unique antinode positions in the map.
    
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
        # Check each pair of antennas with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Compute differences
                dx = x2 - x1
                dy = y2 - y1

                # Antinodes must be along the same line (dx/dy should be rational)
                # Calculate potential antinode positions
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                # Add valid antinodes within bounds
                if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                    antinode_positions.add(antinode1)
                if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                    antinode_positions.add(antinode2)

    return antinode_positions

def main():
    parser = argparse.ArgumentParser(description="Solve Day 8: Resonant Collinearity.")
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
