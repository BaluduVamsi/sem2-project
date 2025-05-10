import numpy as np
import pandas as pd

def odd_magic_square(n):
    magic = np.zeros((n, n), dtype=int)
    num = 1
    i, j = 0, n // 2
    while num <= n ** 2:
        magic[i, j] = num
        num += 1
        newi, newj = (i - 1) % n, (j + 1) % n
        if magic[newi, newj]:
            i += 1
        else:
            i, j = newi, newj
    return pd.DataFrame(magic)

def doubly_even_magic_square(n):
    magic = np.arange(1, n * n + 1).reshape(n, n)
    mask = ((np.indices((n, n)).sum(axis=0) % 4 == 0) |
            ((np.indices((n, n))[0] % 4 == 3) & (np.indices((n, n))[1] % 4 == 0)))
    magic[mask] = (n * n + 1) - magic[mask]
    return pd.DataFrame(magic)

for i in range(4, 9):
    print(f"Magic Square N = {i}")
    if i % 2 == 1:
        print(odd_magic_square(i))
    elif i % 4 == 0:
        print(doubly_even_magic_square(i))
    else:
        print("Magic square for singly-even N (like 6) not implemented.")
