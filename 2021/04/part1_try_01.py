#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Made by ChatGPT — 2025‑12‑03

import sys

def parse_input(lines):
    """
    Parse the puzzle input into a list of draws and a list of boards.
    Each board is a 5x5 list of integers.
    """
    lines = [line.strip() for line in lines]
    draws = [int(x) for x in lines[0].split(',')]
    
    boards = []
    board = []
    for line in lines[2:]:  # skip draws line + first blank
        if line == "":
            if board:
                boards.append(board)
                board = []
        else:
            # split by whitespace (handles multiple spaces)
            row = [int(x) for x in line.split()]
            board.append(row)
    # append last board if any
    if board:
        boards.append(board)
    
    return draws, boards

def mark_number(board, mask, number):
    """
    Mark the number on the board: update mask to True where board == number.
    """
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                mask[i][j] = True

def board_has_won(mask):
    """
    Check if the board has a complete marked row or column.
    """
    # check rows
    for i in range(5):
        if all(mask[i][j] for j in range(5)):
            return True
    # check columns
    for j in range(5):
        if all(mask[i][j] for i in range(5)):
            return True
    return False

def compute_score(board, mask, last_number):
    """
    Sum all unmarked numbers, multiply by last_number.
    """
    total = 0
    for i in range(5):
        for j in range(5):
            if not mask[i][j]:
                total += board[i][j]
    return total * last_number

def find_first_winner_score(draws, boards):
    """
    Simulate the bingo draws; return score of first board that wins.
    """
    # create a mask (False = unmarked, True = marked) for each board
    masks = [ [ [False]*5 for _ in range(5) ] for _ in boards ]
    
    for number in draws:
        # mark number on all boards
        for b_idx, board in enumerate(boards):
            mark_number(board, masks[b_idx], number)
        # after marking, check for any winner
        for b_idx, mask in enumerate(masks):
            if board_has_won(mask):
                return compute_score(boards[b_idx], mask, number)
    return None  # no winner found

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        # Use the example from the problem description
        example = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
        lines = example.splitlines()
    else:
        # read from input.txt
        try:
            with open("input.txt", "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("Error: input.txt not found. Or use --test for the example input.", file=sys.stderr)
            sys.exit(1)
    
    draws, boards = parse_input(lines)
    score = find_first_winner_score(draws, boards)
    if score is None:
        print("No winning board found.")
    else:
        print("First winning board score:", score)

if __name__ == "__main__":
    main()
