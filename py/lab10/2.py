import numpy as np
import pandas as pd

def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row, solutions):
    if row == 8:
        solutions.append(board.copy())
        return
    for col in range(8):
        if is_valid(board, row, col):
            board[row] = col
            solve(board, row + 1, solutions)

board = [-1]*8
solutions = []
solve(board, 0, solutions)

df = pd.DataFrame(solutions)
print(df)
print(len(solutions))

