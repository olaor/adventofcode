def extract_digits(s):
    """Extracts the first and last digit from a given string."""
    digits = [char for char in s if char.isdigit()]
    if len(digits) >= 2:
        return int(digits[0] + digits[-1])
    elif len(digits) == 1:
        return int(digits[0] * 2)  # If only one digit, use it twice
    else:
        return 0  # No digits found

def calculate_calibration_sum(lines):
    """Calculates the sum of calibration values from a list of lines."""
    return sum(extract_digits(line) for line in lines)

calibration_document = open("input.txt").readlines()

total_calibration_value = calculate_calibration_sum(calibration_document)
print(f"Total Calibration Value: {total_calibration_value}")
