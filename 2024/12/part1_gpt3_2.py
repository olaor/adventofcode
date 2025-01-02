import sys
import os
from collections import deque

def read_input(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def get_neighbors(r, c, rows, cols):
    """ Get the valid neighboring coordinates (up, down, left, right) within the bounds of the garden map. """
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if r < rows - 1:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))
    return neighbors

def calculate_perimeter_and_area(r, c, garden_map, visited):
    """ Perform a DFS to calculate the perimeter and area of the region starting at (r, c). """
    rows, cols = len(garden_map), len(garden_map[0])
    stack = [(r, c)]
    visited.add((r, c))
    area = 0
    perimeter = 0
    
    while stack:
        cr, cc = stack.pop()
        area += 1
        for nr, nc in get_neighbors(cr, cc, rows, cols):
            if garden_map[nr][nc] == garden_map[r][c] and (nr, nc) not in visited:
                visited.add((nr, nc))
                stack.append((nr, nc))
            else:
                perimeter += 1  # It's a boundary of the region
    
    return area, perimeter

def main(filename):
    garden_map = read_input(filename)
    rows, cols = len(garden_map), len(garden_map[0])
    visited = set()
    total_cost = 0
    
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                area, perimeter = calculate_perimeter_and_area(r, c, garden_map, visited)
                total_cost += area * perimeter
    
    print("Total fencing cost:", total_cost)

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != '-f':
        print("Usage: python script.py -f <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[2]
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)
    
    main(input_file)

