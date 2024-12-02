# Made by ChatGPT - 2024-12-02
# Script to calculate the number of safe reports, including the Problem Dampener.

import sys

def is_safe_report(report):
    """
    Determine if a report (list of levels) is safe without any modifications.
    A report is safe if:
    1. The levels are either all increasing or all decreasing.
    2. Any two adjacent levels differ by at least 1 and at most 3.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are within the range [1, 3] (increasing)
    increasing = all(1 <= diff <= 3 for diff in differences)
    
    # Check if all differences are within the range [-3, -1] (decreasing)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    return increasing or decreasing

def is_safe_with_dampener(report):
    """
    Determine if a report can be made safe by removing at most one level.
    """
    if is_safe_report(report):
        return True  # Already safe
    
    # Check if removing one level makes the report safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    
    return False

def count_safe_reports(filepath):
    """
    Count the number of safe reports in the input file.
    Each line in the file represents a report.
    """
    safe_count = 0
    
    with open(filepath, 'r') as file:
        for line in file:
            # Convert the line into a list of integers
            report = list(map(int, line.split()))
            if is_safe_with_dampener(report):
                safe_count += 1
                
    return safe_count

def main():
    # Parse command-line arguments
    if '-f' not in sys.argv:
        print("Usage: python script.py -f <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[sys.argv.index('-f') + 1]
    
    try:
        safe_count = count_safe_reports(input_file)
        print(f"Number of safe reports: {safe_count}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
