"""
Made by ChatGPT
Date: 2024-12-10

Day 10: Hoof It - Calculate the sum of the scores of all trailheads in a topographic map.
"""

import argparse
from collections import deque

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

def bfs_find_nines(map_data, start):
    """Performs BFS to find reachable positions with height 9."""
    rows, cols = len(map_data), len(map_data[0])
    visited = set()
    queue = deque([start])
    reachable_nines = set()
    
    while queue:
        x, y = queue.popleft()
        current_height = map_data[x][y]
        
        # Debug: Current position and height
        print(f"Visiting ({x}, {y}) with height {current_height}")
        
        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                next_height = map_data[nx][ny]
                
                # Gradual uphill slope
                if next_height == current_height + 1:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                
                # End of trail at height 9
                if next_height == 9 and current_height == 8 and (nx, ny) not in reachable_nines:
                    reachable_nines.add((nx, ny))
                    visited.add((nx, ny))  # Mark this 9 as visited to prevent revisiting
    
    # Debug: Reachable 9s for this trailhead
    print(f"Trailhead at {start} can reach 9s at: {reachable_nines}")
    
    return reachable_nines

def score_trailhead(map_data, start):
    """Calculates the score for a single trailhead."""
    reachable_nines = bfs_find_nines(map_data, start)
    return len(reachable_nines)

def calculate_total_score(map_data):
    """Calculates the total score of all trailheads."""
    trailheads = find_trailheads(map_data)
    total_score = 0
    for trailhead in trailheads:
        score = score_trailhead(map_data, trailhead)
        print(f"Trailhead at {trailhead} has score: {score}")  # Debug: Score per trailhead
        total_score += score
    return total_score

def main():
    parser = argparse.ArgumentParser(description="Calculate the sum of the scores of all trailheads.")
    parser.add_argument("-f", "--file", required=True, help="Path to the input file containing the topographic map.")
    args = parser.parse_args()
    
    map_data = parse_input(args.file)
    total_score = calculate_total_score(map_data)
    print(f"Total Score: {total_score}")

if __name__ == "__main__":
    main()
