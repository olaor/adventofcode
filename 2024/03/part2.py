#!/usr/bin/env python3
"""
Made by ChatGPT
Date: 2024-12-03

This script parses a corrupted input file for valid mul(X,Y) instructions,
taking into account do() and don't() directives to enable or disable
the execution of mul instructions.

Usage:
    python3 mull_it_over_part2.py -f <input_file>
"""

import re
import argparse

def parse_and_sum_with_conditions(file_path):
    """
    Parse the input file for valid mul(X,Y) instructions, evaluate them
    based on the most recent do() or don't() directive, and return their sum.

    Args:
        file_path (str): Path to the input file.

    Returns:
        int: The sum of all valid mul(X,Y) results, respecting do()/don't() conditions.
    """
    # Regular expressions to match valid mul(X,Y), do(), and don't() instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")

    total_sum = 0
    is_enabled = True  # mul instructions are enabled by default

    with open(file_path, 'r') as f:
        content = f.read()

    # Scan the file for instructions in order
    instructions = re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", content)
    for match in instructions:
        instruction = match.group(0)

        if do_pattern.match(instruction):
            is_enabled = True
        elif dont_pattern.match(instruction):
            is_enabled = False
        elif mul_pattern.match(instruction) and is_enabled:
            x, y = map(int, mul_pattern.match(instruction).groups())
            total_sum += x * y

    return total_sum

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Solve the Mull It Over puzzle (Part 2).")
    parser.add_argument("-f", "--file", required=True, help="Input file containing corrupted memory.")
    args = parser.parse_args()

    try:
        result = parse_and_sum_with_conditions(args.file)
        print(f"The total sum of valid mul(X,Y) instructions is: {result}")
    except FileNotFoundError:
        print(f"Error: The file {args.file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
