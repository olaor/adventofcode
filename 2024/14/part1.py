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

def simulate_robots(robots, width, height, time):
    """
    Simulates the movement of robots within the specified grid for the given time.
    """
    final_positions = []
    for (px, py), (vx, vy) in robots:
        # Calculate new position after 'time' seconds, applying wraparound
        new_x = (px + vx * time) % width
        new_y = (py + vy * time) % height
        final_positions.append((new_x, new_y))
    return final_positions

def count_quadrants(positions, width, height):
    """
    Counts the number of robots in each quadrant of the grid.
    """
    half_width = width // 2
    half_height = height // 2

    quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

    for x, y in positions:
        if x == half_width or y == half_height:
            # Skip robots in the middle
            continue
        if x < half_width and y < half_height:
            quadrants[0] += 1  # Top-left
        elif x >= half_width and y < half_height:
            quadrants[1] += 1  # Top-right
        elif x < half_width and y >= half_height:
            quadrants[2] += 1  # Bottom-left
        else:
            quadrants[3] += 1  # Bottom-right

    return quadrants

def calculate_safety_factor(quadrants):
    """
    Calculates the safety factor by multiplying the robot counts in all quadrants.
    """
    factor = 1
    for count in quadrants:
        factor *= count
    return factor

def main():
    parser = argparse.ArgumentParser(description="Predict robot positions and calculate safety factor.")
    parser.add_argument('-f', '--file', required=True, help="Path to the input file")
    args = parser.parse_args()

    # Parameters
    GRID_WIDTH = 101
    GRID_HEIGHT = 103
    SIMULATION_TIME = 100

    # Parse input
    robots = parse_input(args.file)

    # Simulate robots' movements
    final_positions = simulate_robots(robots, GRID_WIDTH, GRID_HEIGHT, SIMULATION_TIME)

    # Count robots in each quadrant
    quadrants = count_quadrants(final_positions, GRID_WIDTH, GRID_HEIGHT)

    # Calculate safety factor
    safety_factor = calculate_safety_factor(quadrants)

    print(f"Safety Factor after {SIMULATION_TIME} seconds: {safety_factor}")

if __name__ == "__main__":
    main()
