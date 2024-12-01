import sys

def is_adjacent_to_symbol(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] in '*#+$':
            return True
    return False

def sum_part_numbers(grid):
    total_sum = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col].isdigit() and is_adjacent_to_symbol(grid, row, col):
                total_sum += int(grid[row][col])
    return total_sum

def main():
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input_file>")
        return

    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]

    result = sum_part_numbers(grid)
    print(result)

if __name__ == "__main__":
    main()