"""
Made by ChatGPT
Date: 2024-12-10

Day 10: Hoof It - Calculate the sum of the ratings of all trailheads in a topographic map.
"""

import argparse
from functools import lru_cache

def parse_input(file_path):
    """Reads the topographic map from the input file."""
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads(map_data):
    """Finds all trailheads (positions with height 0) on the map."""
    trailheads = []
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            if map_data[row][col] == 0:
                trailheads.append((row, col))
    return trailheads

def count_trails_from(map_data, x, y):
    """Counts all distinct hiking trails starting from (x, y) to height 9."""
    rows, cols = len(map_data), len(map_data[0])
    
    @lru_cache(None)
    def dfs(x, y):
        # Base case: If the current position is height 9, this is a valid trail.
        if map_data[x][y] == 9:
            return 1
        
        total_trails = 0
        current_height = map_data[x][y]
        
        # Explore all four possible directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                next_height = map_data[nx][ny]
                if next_height == current_height + 1:  # Valid uphill step
                    total_trails += dfs(nx, ny)
        
        return total_trails

    # Start the recursive trail counting from the given position
    return dfs(x, y)

def calculate_total_rating(map_data):
    """Calculates the total rating of all trailheads."""
    trailheads = find_trailheads(map_data)
    total_rating = 0
    for trailhead in trailheads:
        rating = count_trails_from(map_data, *trailhead)
        print(f"Trailhead at {trailhead} has rating: {rating}")  # Debug: Rating per trailhead
        total_rating += rating
    return total_rating

def main():
    parser = argparse.ArgumentParser(description="Calculate the sum of the ratings of all trailheads.")
    parser.add_argument("-f", "--file", required=True, help="Path to the input file containing the topographic map.")
    args = parser.parse_args()
    
    map_data = parse_input(args.file)
    total_rating = calculate_total_rating(map_data)
    print(f"Total Rating: {total_rating}")

if __name__ == "__main__":
    main()
