import pandas as pd

asking_prices = pd.Series([1000, 2000, 3000, 1500])
fair_prices = pd.Series([1200, 2500, 2900, 1600])
good_deals = list((asking_prices < fair_prices).where(lambda x: x).dropna().index)
print(good_deals)
