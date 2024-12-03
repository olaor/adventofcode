#!/usr/bin/env python3
"""
Made by ChatGPT
Date: 2024-12-03

This script parses a corrupted input file for valid mul(X,Y) instructions,
evaluates them, and computes their sum.

Usage:
    python3 mull_it_over.py -f <input_file>
"""

import re
import argparse

def parse_and_sum(file_path):
    """
    Parse the input file for valid mul(X,Y) instructions, evaluate them, and return their sum.

    Args:
        file_path (str): Path to the input file.

    Returns:
        int: The sum of all valid mul(X,Y) results.
    """
    # Regular expression to match valid mul(X,Y) instructions
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    total_sum = 0

    with open(file_path, 'r') as f:
        content = f.read()

    # Find all valid mul(X,Y) instructions
    matches = pattern.findall(content)
    for x, y in matches:
        total_sum += int(x) * int(y)

    return total_sum

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Solve the Mull It Over puzzle.")
    parser.add_argument("-f", "--file", required=True, help="Input file containing corrupted memory.")
    args = parser.parse_args()

    try:
        result = parse_and_sum(args.file)
        print(f"The total sum of valid mul(X,Y) instructions is: {result}")
    except FileNotFoundError:
        print(f"Error: The file {args.file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
