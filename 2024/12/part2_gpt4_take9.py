#!/usr/bin/env python3
"""
Made by ChatGPT
Date: 2024-12-16

Solve Part Two of the "Garden Groups" puzzle from Advent of Code 2023.
"""

import argparse
from collections import deque

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Solve the Garden Groups puzzle - Part Two.")
    parser.add_argument('-f', '--file', required=True, help="Input file containing the garden map.")
    return parser.parse_args()

def read_map(file_path):
    """Read the garden map from the input file."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def calculate_area_and_edges(grid, x, y, visited):
    """
    Calculate the area and unique edges of a region using BFS.
    - Area: Number of cells in the region.
    - Edges: Unique straight sections of the fence (external + internal shared).
    """
    plant_type = grid[x][y]
    queue = deque([(x, y)])
    visited.add((x, y))

    area = 0
    edges = set()  # Store unique edges as tuples

    while queue:
        cx, cy = queue.popleft()
        area += 1

        # Each cell has 4 potential edges (top, bottom, left, right)
        # Represent edges as (point1, point2), sorted for uniqueness
        neighbors = [
            ((cx, cy), (cx, cy + 1)),  # Right edge
            ((cx, cy), (cx + 1, cy)),  # Bottom edge
            ((cx, cy - 1), (cx, cy)),  # Left edge
            ((cx - 1, cy), (cx, cy))   # Top edge
        ]

        for edge in neighbors:
            point1, point2 = edge
            if 0 <= point2[0] < len(grid) and 0 <= point2[1] < len(grid[0]):
                nx, ny = point2
                if grid[nx][ny] == plant_type:
                    # If neighbor is part of the same region, don't add the edge
                    continue

            # Add edge as unique
            edges.add(tuple(sorted(edge)))

    return area, len(edges)

def calculate_total_price(grid):
    """Calculate the total price for fencing all regions."""
    visited = set()
    total_price = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                area, edge_count = calculate_area_and_edges(grid, x, y, visited)
                total_price += area * edge_count

    return total_price

def main():
    args = parse_args()
    garden_map = read_map(args.file)
    total_price = calculate_total_price(garden_map)
    print(f"Total price for fencing all regions: {total_price}")

if __name__ == "__main__":
    main()
