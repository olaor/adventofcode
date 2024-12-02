"""
Made by ChatGPT
Date: 2024-12-02

Day 3: Gear Ratios (Part 2)
This script calculates the sum of gear ratios in an engine schematic.
"""
import sys
import argparse
import re

def read_input_file(file_path):
    """Reads the input file and returns the schematic as a list of strings."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def is_digit_or_period(char):
    """Determines if a character is a digit or a period."""
    return char.isdigit() or char == '.'

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

def extract_full_number_at(schematic, x, y):
    """Extracts the full multi-digit number starting at (x, y)."""
    cols = len(schematic[0])
    start_col = y
    end_col = y

    # Expand to the left
    while start_col > 0 and schematic[x][start_col - 1].isdigit():
        start_col -= 1
    # Expand to the right
    while end_col < cols - 1 and schematic[x][end_col + 1].isdigit():
        end_col += 1

    return int(schematic[x][start_col:end_col + 1])

def calculate_gear_ratios(schematic):
    """Calculates the sum of all gear ratios in the schematic."""
    rows = len(schematic)
    cols = len(schematic[0])
    total_gear_ratio = 0

    for x in range(rows):
        for y in range(cols):
            if schematic[x][y] == '*':
                # Extract adjacent positions
                adjacent_positions = get_adjacent_positions(x, y, rows, cols)
                adjacent_numbers = []

                for nx, ny in adjacent_positions:
                    if schematic[nx][ny].isdigit():
                        # Extract the full number at this position
                        full_number = extract_full_number_at(schematic, nx, ny)
                        if full_number not in adjacent_numbers:  # Avoid duplicates
                            adjacent_numbers.append(full_number)

                if len(adjacent_numbers) == 2:
                    gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
                    print(f"Gear at ({x}, {y}) with numbers {adjacent_numbers}: Gear Ratio = {gear_ratio}")
                    total_gear_ratio += gear_ratio

    return total_gear_ratio

def main():
    parser = argparse.ArgumentParser(description="Calculate the sum of gear ratios in an engine schematic.")
    parser.add_argument('-f', '--file', required=True, help="Path to the input file containing the engine schematic.")
    args = parser.parse_args()

    try:
        schematic = read_input_file(args.file)
        result = calculate_gear_ratios(schematic)
        print(f"Total sum of gear ratios: {result}")
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
