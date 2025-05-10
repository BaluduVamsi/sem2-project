import pandas as pd

data = {
    'artist': ['a', 'b', 'a', 'c', 'a', 'b'],
    'venue': ['x', 'y', 'x', 'y', 'z', 'x'],
    'date': pd.date_range('2021-01-01', periods=6, freq='M')
}
df = pd.DataFrame(data)
df['year_month'] = df['date'].dt.to_period('M')

pivot = pd.DataFrame(index=df['year_month'].unique())

for artist in df['artist'].unique():
    for venue in df['venue'].unique():
        mask = (df['artist'] == artist) & (df['venue'] == venue)
        count = df[mask].groupby('year_month').size()
        pivot[(artist, venue)] = count

pivot = pivot.fillna(0).astype(int)
print(pivot)
