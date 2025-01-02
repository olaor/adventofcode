"""
Made by ChatGPT
Date: 2025-01-02
"""

import argparse
import re
from itertools import product
from math import inf

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

def solve_machine(a_button, b_button, prize, max_presses=100):
    """
    Solve for a single machine to find the minimum tokens required to win the prize.
    """
    a_x, a_y = a_button
    b_x, b_y = b_button
    target_x, target_y = prize
    min_tokens = inf

    # Iterate through all possible press combinations
    for a_presses, b_presses in product(range(max_presses + 1), repeat=2):
        x_move = a_presses * a_x + b_presses * b_x
        y_move = a_presses * a_y + b_presses * b_y

        if x_move == target_x and y_move == target_y:
            tokens = a_presses * 3 + b_presses * 1
            min_tokens = min(min_tokens, tokens)

    return min_tokens if min_tokens != inf else None

def main():
    parser = argparse.ArgumentParser(description="Solve the claw machine puzzle.")
    parser.add_argument("-f", "--file", required=True, help="Input file path")
    args = parser.parse_args()

    machines = parse_input(args.file)
    total_tokens = 0
    prizes_won = 0

    for i, (a_button, b_button, prize) in enumerate(machines):
        min_tokens = solve_machine(a_button, b_button, prize)
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
