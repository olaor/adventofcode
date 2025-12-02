# Made by ChatGPT - 2025-12-02

def is_invalid_id(n):
    """Check if the number consists of a repeated sequence of digits at least twice."""
    s = str(n)
    length = len(s)
    for chunk_size in range(1, length // 2 + 1):
        if length % chunk_size != 0:
            continue
        repetitions = length // chunk_size
        chunk = s[:chunk_size]
        if chunk * repetitions == s and repetitions >= 2:
            return True
    return False

def parse_ranges(line):
    """Parse a line of ranges like '11-22,95-115,...' into a list of (start, end) tuples."""
    ranges = []
    for part in line.strip().split(','):
        if not part:
            continue
        start, end = map(int, part.split('-'))
        ranges.append((start, end))
    return ranges

def find_invalid_ids(ranges):
    invalid_ids = []
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num):
                invalid_ids.append(num)
    return invalid_ids

def main(test=False):
    if test:
        input_line = (
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
            "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
            "824824821-824824827,2121212118-2121212124"
        )
    else:
        with open("input.txt") as f:
            input_line = f.read().strip()

    ranges = parse_ranges(input_line)
    invalid_ids = find_invalid_ids(ranges)
    total = sum(invalid_ids)

    print("Invalid IDs:", invalid_ids)
    print("Sum of invalid IDs:", total)

if __name__ == "__main__":
    # Change to False when running with input.txt
    main(test=False)
