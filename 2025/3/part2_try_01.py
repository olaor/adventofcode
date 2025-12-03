# Made by ChatGPT - 2025-12-03

def max_12_digit_joltage(bank: str) -> int:
    digits_needed = 12
    stack = []
    to_remove = len(bank) - digits_needed

    for digit in bank:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    # Trim to exactly 12 digits (in case the bank had more than needed)
    return int(''.join(stack[:digits_needed]))

def solve_part_two(data: list[str]) -> int:
    return sum(max_12_digit_joltage(line.strip()) for line in data if line.strip())

if __name__ == "__main__":
    # Test mode with example input
    test_data = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]
    print("Test Mode (Part Two): Total Output Joltage =", solve_part_two(test_data))

    # Standard mode with real input
    try:
        with open("input.txt") as f:
            input_data = f.readlines()
        print("Standard Mode (Part Two): Total Output Joltage =", solve_part_two(input_data))
    except FileNotFoundError:
        print("input.txt not found. Please provide your puzzle input in 'input.txt'.")
