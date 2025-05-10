import numpy as np
import pandas as pd

n = 10
points = np.random.rand(n, 2) * 100
df = pd.DataFrame(points, columns=['x', 'y'])
df['r'] = np.sqrt(df['x']**2 + df['y']**2)
df['theta'] = np.arctan2(df['y'], df['x'])
print(df)
