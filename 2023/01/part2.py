def extract_digits(s):
    """Extracts the first and last digit from a given string."""
    digits = [char for char in s if char.isdigit()]
    if len(digits) >= 2:
        return int(digits[0] + digits[-1])
    elif len(digits) == 1:
        return int(digits[0] * 2)  # If only one digit, use it twice
    else:
        return 0  # No digits found

def replace_values(lines):
    digit_map = {
        "one": "1", "two": "2", "three": "3", "four": "4", 
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    output = []
    buffer = ""
    for line in lines:
        tmp = line
        start = end = 0
        for c in tmp:
            buffer += c
            end += 1
            if buffer in digit_map.keys():
                
                
        print(line)
        output.append(line)
    return output

def calculate_calibration_sum(lines):
    """Calculates the sum of calibration values from a list of lines."""
    total = 0
    for line in lines:
        value = extract_digits(line)
        print(line, value)
        total += value 
    return total

calibration_document = open("input.txt").readlines()

calibration_document = replace_values(calibration_document)

total_calibration_value = calculate_calibration_sum(calibration_document)
print(f"Total Calibration Value: {total_calibration_value}")
