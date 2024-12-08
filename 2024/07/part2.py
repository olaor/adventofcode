"""
Bridge Repair Solution - Part Two
Made by ChatGPT - 2024-12-08
"""

import sys
import itertools

def evaluate_expression(numbers, operators):
    """
    Evaluate the expression formed by interleaving numbers with operators.
    Operators are applied left-to-right, including the concatenation operator '||'.
    """
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            # Concatenation: merge digits of result and next number
            result = int(str(result) + str(numbers[i + 1]))
    return result

def is_solvable(target, numbers):
    """
    Determine if the target value can be achieved by placing '+', '*', or '||' between numbers.
    """
    # Number of gaps between numbers
    num_gaps = len(numbers) - 1
    # Generate all combinations of operators for the gaps
    for ops in itertools.product(['+', '*', '||'], repeat=num_gaps):
        try:
            if evaluate_expression(numbers, ops) == target:
                return True
        except ValueError:
            # Handle cases where concatenation fails due to invalid input
            continue
    return False

def calculate_calibration_result(input_file):
    """
    Calculate the total calibration result from the input file.
    """
    total_calibration_result = 0

    with open(input_file, 'r') as file:
        for line in file:
            if ':' not in line:
                continue  # Skip invalid lines
            target, numbers = line.split(':')
            target = int(target.strip())
            numbers = list(map(int, numbers.strip().split()))

            if is_solvable(target, numbers):
                total_calibration_result += target

    return total_calibration_result

if __name__ == "__main__":
    # Ensure the -f parameter is provided
    if "-f" not in sys.argv:
        print("Usage: python bridge_repair.py -f <input_file>")
        sys.exit(1)

    # Get the input file path
    try:
        input_file = sys.argv[sys.argv.index("-f") + 1]
    except IndexError:
        print("Error: No input file specified after -f.")
        sys.exit(1)

    # Calculate and print the result
    result = calculate_calibration_result(input_file)
    print(f"Total Calibration Result: {result}")
