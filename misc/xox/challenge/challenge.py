#!/usr/bin/env python3
import random

def check_winner(board):
    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 'X'
        elif all(board[row][col] == 'O' for row in range(3)):
            return 'O'
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2-i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2-i] == 'O' for i in range(3)):
        return 'O'
    return 'D'

print('here is the result of 1000 person playing X O you must return a string of containing the right sequence to get the flag if x win return x , if o return o else return d : ')
for i in range(1000):
    a = list('XXXXOOOO')
    a.append(random.choice(['X', 'O']))
    random.shuffle(a) 
    tmp = ''.join(a)
    print(tmp)
    board = [list(tmp[i:i+3]) for i in range(0, len(tmp), 3)]

    result = input('enter the results: ')
    if result == check_winner(board):
        print('gg keep going')
    else:
        print('wrong answer')
        exit()

print('AlphaCTF{GG_y0u_knOw_hOw_t0_wr1t3_$cr1p7s}')