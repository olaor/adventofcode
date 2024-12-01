# Made by ChatGPT on 2024-12-01
import argparse
from collections import Counter

def calculate_similarity_score(file_path):
    # Read input from the specified file
    with open(file_path, 'r') as file:
        left_list = []
        right_list = []
        for line in file:
            # Split the line into left and right numbers
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Count occurrences in the right list
    right_counts = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(num * right_counts[num] for num in left_list)
    return similarity_score

def main():
    parser = argparse.ArgumentParser(description="Calculate the similarity score between two lists.")
    parser.add_argument("-f", "--file", required=True, help="Path to the input file.")
    args = parser.parse_args()

    similarity_score = calculate_similarity_score(args.file)
    print(f"The similarity score is: {similarity_score}")

if __name__ == "__main__":
    main()
