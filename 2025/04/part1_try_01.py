#!/usr/bin/env python3
# Made by ChatGPT — ElfOffTheShelf ✨
# Date: 2025‑12‑06

import sys

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

def count_accessible(grid):
    """
    Given grid as list of strings (same length), count how many '@' cells
    have fewer than 4 adjacent '@' in the 8 neighbors.
    """
    H = len(grid)
    W = len(grid[0]) if H > 0 else 0

    accessible = 0

    for r in range(H):
        for c in range(W):
            if grid[r][c] != '@':
                continue

            # count adjacent paper rolls
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
                accessible += 1

    return accessible

def main():
    # If user passes "--test", run on the example
    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t"):
        grid = EXAMPLE.strip().splitlines()
        result = count_accessible(grid)
        print("Example accessible count:", result)
        # Expect 13 for the provided example
    else:
        # Read actual input from "input.txt"
        try:
            with open("input.txt", "r") as f:
                grid = [line.rstrip("\n") for line in f if line.strip()]
        except FileNotFoundError:
            print("Error: input.txt not found.", file=sys.stderr)
            sys.exit(1)

        result = count_accessible(grid)
        print(result)

if __name__ == "__main__":
    main()
