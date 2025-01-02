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

def calculate_area_and_edges(grid, x, y, visited, edges):
    """
    Calculate the area and unique edges of a region using BFS.
    - Area: Number of cells in the region.
    - Edges: Unique straight sections of the fence.
    """
    plant_type = grid[x][y]
    queue = deque([(x, y)])
    visited.add((x, y))

    area = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        cx, cy = queue.popleft()
        area += 1

        # Process each neighbor and track edges
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == plant_type:
                    if (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                else:
                    # Add edge with a neighbor of a different type
                    edge = frozenset([(cx, cy), (nx, ny)])
                    edges.add(edge)
            else:
                # Add edge for boundary (out of bounds)
                edge = frozenset([(cx, cy), (nx, ny)])
                edges.add(edge)

    return area

def calculate_total_price(grid):
    """Calculate the total price for fencing all regions."""
    visited = set()
    total_price = 0
    global_edges = set()  # To track unique edges globally

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in visited:
                edges = set()  # Track edges for this region
                area = calculate_area_and_edges(grid, x, y, visited, edges)
                global_edges.update(edges)
                total_price += area * len(edges)

    return total_price

def main():
    args = parse_args()
    garden_map = read_map(args.file)
    total_price = calculate_total_price(garden_map)
    print(f"Total price for fencing all regions: {total_price}")

if __name__ == "__main__":
    main()
