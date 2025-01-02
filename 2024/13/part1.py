#!/usr/bin/env python3
"""
Made by ChatGPT - ElfOffTheShelf
Date: June 17, 2024

Day 13: Claw Contraption

This program calculates the minimal token cost to win prizes from claw machines
given movement constraints. It reads input from a file specified by the -f parameter.
"""

import argparse
import re

def parse_input(filename):
    """
    Parses the input file to extract button movements and prize positions.

    Args:
        filename (str): Path to the input file.
    
    Returns:
        list: A list of dictionaries containing button and prize data.
    """
    machines = []
    with open(filename, 'r') as file:
        lines = file.readlines()

    pattern_a = r"Button A: X\+(\d+), Y\+(\d+)"
    pattern_b = r"Button B: X\+(\d+), Y\+(\d+)"
    pattern_prize = r"Prize: X=(\d+), Y=(\d+)"

    i = 0
    while i < len(lines):
        if match_a := re.search(pattern_a, lines[i]):
            a_x, a_y = map(int, match_a.groups())
            if match_b := re.search(pattern_b, lines[i+1]):
                b_x, b_y = map(int, match_b.groups())
                if match_prize := re.search(pattern_prize, lines[i+2]):
                    prize_x, prize_y = map(int, match_prize.groups())
                    machines.append({
                        "A": (a_x, a_y),
                        "B": (b_x, b_y),
                        "Prize": (prize_x, prize_y)
                    })
        i += 3
    return machines

def solve_machine(a_move, b_move, prize):
    """
    Solves for the minimum cost to align the claw to the prize position.

    Args:
        a_move (tuple): (x, y) movement for button A.
        b_move (tuple): (x, y) movement for button B.
        prize (tuple): Target (x, y) prize position.

    Returns:
        int: Minimum token cost if possible, else None.
    """
    max_presses = 100
    a_x, a_y = a_move
    b_x, b_y = b_move
    target_x, target_y = prize

    min_cost = float('inf')
    
    for a_presses in range(max_presses + 1):
        for b_presses in range(max_presses + 1):
            total_x = a_presses * a_x + b_presses * b_x
            total_y = a_presses * a_y + b_presses * b_y
            if total_x == target_x and total_y == target_y:
                cost = a_presses * 3 + b_presses * 1
                min_cost = min(min_cost, cost)
    
    return min_cost if min_cost != float('inf') else None

def main():
    """
    Main function to process input, solve machines, and calculate results.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Solve Day 13: Claw Contraption")
    parser.add_argument("-f", "--file", required=True, help="Input file path")
    args = parser.parse_args()

    # Parse the input file
    machines = parse_input(args.file)
    
    total_cost = 0
    prizes_won = 0

    # Process each machine
    for idx, machine in enumerate(machines):
        a_move = machine["A"]
        b_move = machine["B"]
        prize = machine["Prize"]
        
        min_cost = solve_machine(a_move, b_move, prize)
        if min_cost is not None:
            prizes_won += 1
            total_cost += min_cost
            print(f"Machine {idx + 1}: Prize won with cost {min_cost}")
        else:
            print(f"Machine {idx + 1}: No solution found")
    
    print("\nSummary:")
    print(f"Prizes Won: {prizes_won}")
    print(f"Total Cost: {total_cost}")

if __name__ == "__main__":
    main()
