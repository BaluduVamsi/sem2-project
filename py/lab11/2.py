import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])
print(s.str.upper())
print(s.str.lower())
print(s.str.len())
