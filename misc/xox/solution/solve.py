#!/usr/bin/env python3
from pwn import *
def check_winner(board):
    # Check rows
    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 'X'
        elif all(board[row][col] == 'O' for row in range(3)):
            return 'O'
    
    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2-i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2-i] == 'O' for i in range(3)):
        return 'O'
    
    # If no winner
    return 'D'
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

io = process('../challenge/challenge.py')
io.recvline()
for i in range(1000):
    board_str = io.recvline().decode().strip()
    board = [list(board_str[i:i+3]) for i in range(0, len(board_str), 3)]
    winner = check_winner(board)
    io.sendlineafter('enter the results: ', winner)
    print(winner)
    io.recvline()

print(io.recvline())