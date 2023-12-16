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

def is_game_possible(game_data, red, green, blue):
    """Check if a game is possible with given number of cubes."""
    for draw in game_data:
        if draw['red'] > red or draw['green'] > green or draw['blue'] > blue:
            return False
    return True

def solve_puzzle(input_data, red, green, blue):
    """Solve the puzzle with given input data and number of cubes."""
    possible_games = []

    for game_id, game_data in input_data.items():
        if is_game_possible(game_data, red, green, blue):
            possible_games.append(game_id)

    return sum(possible_games)

# File path
file_path = 'input.txt'

# Read input data from the file
input_data = read_input_file(file_path)

# Number of cubes
red_cubes = 12
green_cubes = 13
blue_cubes = 14

# Solve the puzzle
result = solve_puzzle(input_data, red_cubes, green_cubes, blue_cubes)
print("Sum of the IDs of possible games:", result)
