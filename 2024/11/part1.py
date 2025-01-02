# Made by ChatGPT
# Date: 2024-12-11

import sys

def process_stones(stones):
    """
    Processes a single "blink" transformation of the stones according to the rules.
    """
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            # Split stone into two new stones
            digits = str(stone)
            half = len(digits) // 2
            left = int(digits[:half])
            right = int(digits[half:])
            new_stones.extend([left, right])
        else:
            # Replace stone by multiplying with 2024
            new_stones.append(stone * 2024)
    return new_stones

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
            stones = list(map(int, file.read().strip().split()))
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Input file must contain space-separated integers.")
        sys.exit(1)
    
    # Number of blinks to simulate
    num_blinks = 25
    
    # Simulate the blinks
    for _ in range(num_blinks):
        stones = process_stones(stones)
    
    # Output the number of stones after 25 blinks
    print(len(stones))

if __name__ == "__main__":
    main()
