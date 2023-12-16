def parse_game_data(line):
    """Parse a line of game data into a usable format."""
    game_data = []
    parts = line.strip().split(': ')[1].split('; ')
    for part in parts:
        draw_data = {'red': 0, 'green': 0, 'blue': 0}
        cubes = part.split(', ')
        for cube in cubes:
            if cube:
                count, color = cube.split(' ')
                draw_data[color] = int(count)
        game_data.append(draw_data)
    return game_data

def read_input_file(filename):
    """Read and parse the input file."""
    input_data = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('Game'):
                game_id = int(line.split(':')[0].split(' ')[1])
                input_data[game_id] = parse_game_data(line)
    return input_data

def find_minimum_cubes(game_data):
    """Find the minimum number of cubes of each color that must have been in the bag."""
    min_red, min_green, min_blue = 0, 0, 0
    for draw in game_data:
        min_red = max(min_red, draw['red'])
        min_green = max(min_green, draw['green'])
        min_blue = max(min_blue, draw['blue'])
    return min_red, min_green, min_blue

def calculate_power(red, green, blue):
    """Calculate the power of a set of cubes."""
    return red * green * blue

def solve_puzzle_part_two(input_data):
    """Solve the second part of the puzzle."""
    total_power = 0

    for game_id, game_data in input_data.items():
        min_red, min_green, min_blue = find_minimum_cubes(game_data)
        power = calculate_power(min_red, min_green, min_blue)
        total_power += power

    return total_power

# File path
file_path = 'input.txt'

# Read input data from the file
input_data = read_input_file(file_path)

# Solve the second part of the puzzle
result = solve_puzzle_part_two(input_data)
print("Sum of the power of minimum sets:", result)
