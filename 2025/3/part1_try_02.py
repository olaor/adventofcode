# Made by ChatGPT - 2025-12-03

def max_joltage_per_bank(bank: str) -> int:
    max_jolt = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            pair = int(bank[i] + bank[j])
            max_jolt = max(max_jolt, pair)
    return max_jolt

def solve(data: list[str]) -> int:
    return sum(max_joltage_per_bank(line.strip()) for line in data if line.strip())

if __name__ == "__main__":
    # Test mode with example input
    test_data = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]
    print("Test Mode: Total Output Joltage =", solve(test_data))

    # Standard mode with real input
    try:
        with open("input.txt") as f:
            input_data = f.readlines()
        print("Standard Mode: Total Output Joltage =", solve(input_data))
    except FileNotFoundError:
        print("input.txt not found. Please provide your puzzle input in 'input.txt'.")
