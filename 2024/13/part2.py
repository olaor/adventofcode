"""
Made by ChatGPT
Date: 2025-01-02
"""

import argparse
import re
from math import gcd, ceil, floor


def parse_input(file_path):
    """
    Parse the input file to extract the button configurations and prize positions.
    """
    machines = []
    with open(file_path, 'r') as f:
        data = f.read()
        machine_data = data.strip().split("\n\n")
        for machine in machine_data:
            match = re.findall(r"X\+(\d+), Y\+(\d+)|X=(\d+), Y=(\d+)", machine)
            if match:
                a_button = tuple(map(int, match[0][:2]))
                b_button = tuple(map(int, match[1][:2]))
                prize = tuple(map(int, match[2][2:]))
                machines.append((a_button, b_button, prize))
    return machines


def add_prize_offset(machines, offset):
    """
    Add the specified offset to all prize positions.
    """
    return [
        (a_button, b_button, (prize[0] + offset, prize[1] + offset))
        for a_button, b_button, prize in machines
    ]


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm to find x, y such that ax + by = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def solve_linear_diophantine(a, b, target):
    """
    Solve ax + by = target for integers x, y.
    Returns gcd(a, b), x, y if a solution exists, otherwise None.
    """
    g, x, y = extended_gcd(a, b)
    if target % g != 0:
        return None  # No solution exists
    scale = target // g
    return g, x * scale, y * scale


def find_min_cost(a_button, b_button, prize):
    """
    Find the minimum cost to win the prize for one machine.
    """
    a_x, a_y = a_button
    b_x, b_y = b_button
    x_target, y_target = prize

    # Solve for X-axis
    x_result = solve_linear_diophantine(a_x, b_x, x_target)
    if x_result is None:
        return None  # No solution for X-axis
    g_x, x1, y1 = x_result

    # Solve for Y-axis
    y_result = solve_linear_diophantine(a_y, b_y, y_target)
    if y_result is None:
        return None  # No solution for Y-axis
    g_y, x2, y2 = y_result

    # Determine step sizes for parameterization
    step_x = b_x // g_x
    step_y = b_y // g_y

    # Minimize cost using parameterized solutions
    min_cost = float('inf')
    best_a = best_b = None

    for k in range(-1000, 1000):  # Adjust range if necessary
        a_presses = x1 + k * step_x
        b_presses = y1 + k * step_y

        # Ensure non-negative solutions
        if a_presses >= 0 and b_presses >= 0:
            cost = 3 * a_presses + b_presses
            if cost < min_cost:
                min_cost = cost
                best_a = a_presses
                best_b = b_presses

    return min_cost if min_cost != float('inf') else None


def main():
    parser = argparse.ArgumentParser(description="Solve the claw machine puzzle.")
    parser.add_argument("-f", "--file", required=True, help="Input file path")
    args = parser.parse_args()

    offset = 10**13
    machines = parse_input(args.file)
    machines = add_prize_offset(machines, offset)

    total_tokens = 0
    prizes_won = 0

    for i, (a_button, b_button, prize) in enumerate(machines):
        min_tokens = find_min_cost(a_button, b_button, prize)
        if min_tokens is not None:
            prizes_won += 1
            total_tokens += min_tokens
            print(f"Machine {i+1}: Prize won with {min_tokens} tokens.")
        else:
            print(f"Machine {i+1}: Prize cannot be won.")

    print(f"\nTotal prizes won: {prizes_won}")
    print(f"Minimum total tokens spent: {total_tokens}")


if __name__ == "__main__":
    main()

