# Made by ChatGPT
# Date: 2024-12-11

import sys
from collections import Counter

def split_stone(stone):
    """
    Splits a stone into two stones based on its digits.
    """
    digits = str(stone)
    half = len(digits) // 2
    left = int(digits[:half])
    right = int(digits[half:])
    return left, right

def process_stones_optimized(stone_counts):
    """
    Processes stones for one blink using a Counter to optimize memory and computation.
    """
    new_stone_counts = Counter()
    for stone, count in stone_counts.items():
        if stone == 0:
            # Rule 1: Replace 0 with 1
            new_stone_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            # Rule 2: Split stone
            left, right = split_stone(stone)
            new_stone_counts[left] += count
            new_stone_counts[right] += count
        else:
            # Rule 3: Multiply by 2024
            new_stone_counts[stone * 2024] += count
    return new_stone_counts

def main():
    """
    Main function to read input, process the blinks, and output the result.
    """
    # Parse the command-line argument for the input file
    if '-f' not in sys.argv:
        print("Usage: python script.py -f <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[sys.argv.index('-f') + 1]
    
    try:
        with open(input_file, 'r') as file:
            initial_stones = list(map(int, file.read().strip().split()))
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Input file must contain space-separated integers.")
        sys.exit(1)
    
    # Initialize stone counts
    stone_counts = Counter(initial_stones)
    
    # Number of blinks to simulate
    num_blinks = 75
    
    # Simulate the blinks
    for _ in range(num_blinks):
        stone_counts = process_stones_optimized(stone_counts)
    
    # Output the total number of stones after 75 blinks
    print(sum(stone_counts.values()))

if __name__ == "__main__":
    main()

