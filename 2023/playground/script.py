# Made by ChatGPT - ElfOffTheShelf
# Date: 2023-12-21

from collections import deque

def read_map(filename='input.txt'):
    """Reads the garden map from a file and returns the map and starting position."""
    with open(filename) as file:
        garden_map = [list(line.strip()) for line in file]
    for y, row in enumerate(garden_map):
        for x, cell in enumerate(row):
            if cell == 'S':
                return garden_map, (x, y)
    raise ValueError("Starting position 'S' not found in the map.")

def bfs(garden_map, start, steps):
    """Performs a BFS to count reachable garden plots exactly 'steps' away."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, 0)])  # (position, step_count)
    visited = set([start])
    reachable_plots = set()

    while queue:
        (x, y), step_count = queue.popleft()

        if step_count == steps:
            reachable_plots.add((x, y))
        elif step_count < steps:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(garden_map[0]) and 0 <= ny < len(garden_map) and \
                   garden_map[ny][nx] == '.' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), step_count + 1))

    return reachable_plots

def main():
    garden_map, start = read_map()
    reachable_plots = bfs(garden_map, start, 64)
    print("Number of garden plots reachable in exactly 64 steps:", len(reachable_plots))

if __name__ == "__main__":
    main()

