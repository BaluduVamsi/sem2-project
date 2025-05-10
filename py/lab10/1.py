import numpy as np
import random

def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_queens(board, row):
    if row == 8:
        return board
    for col in range(8):
        if is_valid(board, row, col):
            board[row] = col
            result = solve_queens(board, row + 1)
            if result:
                return result
    return None

board = [-1] * 8
solution = solve_queens(board, 0)
print(solution)
