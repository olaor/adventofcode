"""
Made by ChatGPT
Date: 2024-12-02

Day 3: Gear Ratios
This script calculates the total sum of "part numbers" in an engine schematic.
"""
import sys
import argparse
import re

def read_input_file(file_path):
    """Reads the input file and returns the schematic as a list of strings."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def is_symbol(char):
    """Determines if a character is considered a symbol."""
    return char not in "0123456789."

def get_adjacent_positions(x, y, max_rows, max_cols):
    """Returns all valid adjacent positions (including diagonals) for a given position."""
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Upper row
        (0, -1),         (0, 1),     # Same row
        (1, -1), (1, 0), (1, 1)      # Lower row
    ]
    return [
        (x + dx, y + dy)
        for dx, dy in directions
        if 0 <= x + dx < max_rows and 0 <= y + dy < max_cols
    ]

def extract_part_numbers(schematic):
    """Finds all part numbers and determines if they are adjacent to symbols."""
    rows = len(schematic)
    cols = len(schematic[0])
    total_sum = 0

    for x in range(rows):
        for match in re.finditer(r"\d+", schematic[x]):
            # Extract part number and its start/end positions
            part_number = int(match.group())
            start, end = match.start(), match.end() - 1
            
            # Check adjacency for any part of the number
            is_part = any(
                is_symbol(schematic[nx][ny])
                for pos in range(start, end + 1)
                for nx, ny in get_adjacent_positions(x, pos, rows, cols)
            )
            if is_part:
                total_sum += part_number

    return total_sum

def main():
    parser = argparse.ArgumentParser(description="Calculate the sum of part numbers in an engine schematic.")
    parser.add_argument('-f', '--file', required=True, help="Path to the input file containing the engine schematic.")
    args = parser.parse_args()

    try:
        schematic = read_input_file(args.file)
        result = extract_part_numbers(schematic)
        print(f"Total sum of part numbers: {result}")
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
