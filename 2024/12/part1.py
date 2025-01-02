#!/usr/bin/env python3
"""
Made by ChatGPT
Date: 2024-12-13

Solve the "Garden Groups" puzzle from Advent of Code 2023.
"""

import argparse
from collections import deque

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Solve the Garden Groups puzzle.")
    parser.add_argument('-f', '--file', required=True, help="Input file containing the garden map.")
    return parser.parse_args()

def read_map(file_path):
    """Read the garden map from the input file."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def calculate_area_and_perimeter(grid, x, y, visited):
    """Calculate the area and perimeter of a region using BFS."""
    plant_type = grid[x][y]
    queue = deque([(x, y)])
    visited.add((x, y))

    area = 0
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        cx, cy = queue.popleft()
        area += 1
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == plant_type and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                elif grid[nx][ny] != plant_type:
                    perimeter += 1
            else:
                # Edge of the grid contributes to perimeter
                perimeter += 1

    return area, perimeter

def calculate_total_price(grid):
    """Calculate the total price for fencing all regions."""
    visited = set()
    total_price = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                area, perimeter = calculate_area_and_perimeter(grid, x, y, visited)
                total_price += area * perimeter

    return total_price

def main():
    args = parse_args()
    garden_map = read_map(args.file)
    total_price = calculate_total_price(garden_map)
    print(f"Total price for fencing all regions: {total_price}")

if __name__ == "__main__":
    main()
