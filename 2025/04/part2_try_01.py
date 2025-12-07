#!/usr/bin/env python3
# Made by ChatGPT — ElfOffTheShelf ✨
# Date: 2025‑12‑06

import sys
import copy

EXAMPLE = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def count_accessible_positions(grid):
    H = len(grid)
    W = len(grid[0]) if H > 0 else 0
    to_remove = set()

    for r in range(H):
        for c in range(W):
            if grid[r][c] != '@':
                continue

            adj = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < H and 0 <= cc < W:
                        if grid[rr][cc] == '@':
                            adj += 1

            if adj < 4:
                to_remove.add((r, c))

    return to_remove

def simulate_removal(grid):
    total_removed = 0
    grid = [list(row) for row in grid]  # convert to mutable grid

    while True:
        to_remove = count_accessible_positions(grid)
        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'  # remove the roll

        total_removed += len(to_remove)

    return total_removed

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t"):
        grid = EXAMPLE.strip().splitlines()
        result = simulate_removal(grid)
        print("Example total removed rolls:", result)
        # Expect 43 for the provided example
    else:
        try:
            with open("input.txt", "r") as f:
                grid = [line.rstrip("\n") for line in f if line.strip()]
        except FileNotFoundError:
            print("Error: input.txt not found.", file=sys.stderr)
            sys.exit(1)

        result = simulate_removal(grid)
        print(result)

if __name__ == "__main__":
    main()
