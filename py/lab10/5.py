import numpy as np
import pandas as pd

arr = np.array(['one', 'two', 'three', 'longerword'])
centered = np.char.center(arr, 15, '_')
left = np.char.ljust(arr, 15, '_')
right = np.char.rjust(arr, 15, '_')
df = pd.DataFrame({'center': centered, 'left': left, 'right': right})
print(df)
