#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Made by ChatGPT — 2025‑12‑03

import sys

def parse_input(lines):
    lines = [line.strip() for line in lines]
    draws = [int(x) for x in lines[0].split(',')]
    
    boards = []
    board = []
    for line in lines[2:]:
        if line == "":
            if board:
                boards.append(board)
                board = []
        else:
            row = [int(x) for x in line.split()]
            board.append(row)
    if board:
        boards.append(board)
    
    return draws, boards

def mark_number(board, mask, number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                mask[i][j] = True

def board_has_won(mask):
    for i in range(5):
        if all(mask[i][j] for j in range(5)):
            return True
    for j in range(5):
        if all(mask[i][j] for i in range(5)):
            return True
    return False

def compute_score(board, mask, last_number):
    total = 0
    for i in range(5):
        for j in range(5):
            if not mask[i][j]:
                total += board[i][j]
    return total * last_number

def find_first_winner_score(draws, boards):
    masks = [ [ [False]*5 for _ in range(5) ] for _ in boards ]
    
    for number in draws:
        for b_idx, board in enumerate(boards):
            mark_number(board, masks[b_idx], number)
        for b_idx, mask in enumerate(masks):
            if board_has_won(mask):
                return compute_score(boards[b_idx], mask, number)
    return None

def find_last_winner_score(draws, boards):
    masks = [ [ [False]*5 for _ in range(5) ] for _ in boards ]
    won = set()
    last_score = None

    for number in draws:
        for b_idx, board in enumerate(boards):
            if b_idx in won:
                continue
            mark_number(board, masks[b_idx], number)
            if board_has_won(masks[b_idx]):
                won.add(b_idx)
                last_score = compute_score(board, masks[b_idx], number)
    return last_score

def main():
    if "--test" in sys.argv:
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
        try:
            with open("input.txt", "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("Error: input.txt not found. Or use --test.", file=sys.stderr)
            sys.exit(1)

    draws, boards = parse_input(lines)
    
    if "--last" in sys.argv:
        score = find_last_winner_score(draws, boards)
        print("Last winning board score:", score)
    else:
        score = find_first_winner_score(draws, boards)
        print("First winning board score:", score)

if __name__ == "__main__":
    main()
