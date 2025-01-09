"""
Made by ChatGPT
Date: 2025-01-03
"""

import argparse

def parse_input(file_path):
    """
    Parses the input file to extract robot positions and velocities.
    """
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                position_part, velocity_part = line.split(' ')
                px, py = map(int, position_part[2:].split(','))
                vx, vy = map(int, velocity_part[2:].split(','))
                robots.append(((px, py), (vx, vy)))
    return robots

def simulate_positions(robots, time):
    """
    Simulates the positions of robots at a given time step.
    """
    positions = []
    for (px, py), (vx, vy) in robots:
        new_x = px + vx * time
        new_y = py + vy * time
        positions.append((new_x, new_y))
    return positions

def find_bounding_box(positions):
    """
    Finds the bounding box (min_x, min_y, max_x, max_y) for a set of positions.
    """
    min_x = min(pos[0] for pos in positions)
    max_x = max(pos[0] for pos in positions)
    min_y = min(pos[1] for pos in positions)
    max_y = max(pos[1] for pos in positions)
    return min_x, min_y, max_x, max_y

def bounding_box_area(positions):
    """
    Calculates the area of the bounding box enclosing the positions.
    """
    min_x, min_y, max_x, max_y = find_bounding_box(positions)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    return width * height

def print_positions(positions):
    """
    Prints the current positions of robots as a grid.
    """
    min_x, min_y, max_x, max_y = find_bounding_box(positions)
    grid = [['.' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]
    for x, y in positions:
        grid[y - min_y][x - min_x] = '#'
    for row in grid:
        print(''.join(row))

def is_christmas_tree(positions):
    """
    Checks if the current positions form a Christmas tree shape.
    """
    min_x, min_y, max_x, max_y = find_bounding_box(positions)
    height = max_y - min_y + 1
    width = max_x - min_x + 1

    # Christmas tree requires height > width
    if height <= width:
        return False

    # Map positions to grid
    grid = set(positions)

    # Check for triangular shape: each row must have fewer positions as you go up
    for y in range(max_y, min_y - 1, -1):
        row_positions = [x for x, row_y in positions if row_y == y]
        if len(row_positions) != (max_y - y + 1):
            return False
        # Ensure positions are centered
        if len(row_positions) > 1:
            expected_min = min_x + (max_y - y)
            expected_max = max_x - (max_y - y)
            if not all(expected_min <= x <= expected_max for x in row_positions):
                return False

    return True

def find_christmas_tree(robots):
    """
    Optimized search for when robots form a Christmas tree-like shape.
    """
    time = 0
    previous_area = float('inf')
    compact_time = -1
    max_search_steps = 1000  # To prevent infinite loops

    for step in range(max_search_steps):
        positions = simulate_positions(robots, time)
        area = bounding_box_area(positions)

        if area < previous_area:
            previous_area = area
            compact_time = time
        elif area > previous_area:
            # If area increases, assume we've passed the most compact configuration
            break

        if is_christmas_tree(positions):
            print(f"Easter egg found at time: {time}")
            print_positions(positions)
            return time

        time += 1

    print(f"Most compact configuration found at time: {compact_time}")
    return compact_time

def main():
    parser = argparse.ArgumentParser(description="Find the fewest seconds for robots to display an Easter egg.")
    parser.add_argument('-f', '--file', required=True, help="Path to the input file")
    args = parser.parse_args()

    # Parse input
    robots = parse_input(args.file)

    # Find Christmas tree
    find_christmas_tree(robots)

if __name__ == "__main__":
    main()
