# Made by ChatGPT on 2024-12-01
import argparse

def calculate_total_distance(file_path):
    # Read input from the specified file
    with open(file_path, 'r') as file:
        left_list = []
        right_list = []
        for line in file:
            # Split the line into left and right numbers
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance

def main():
    parser = argparse.ArgumentParser(description="Calculate the total distance between two lists.")
    parser.add_argument("-f", "--file", required=True, help="Path to the input file.")
    args = parser.parse_args()

    total_distance = calculate_total_distance(args.file)
    print(f"The total distance is: {total_distance}")

if __name__ == "__main__":
    main()
