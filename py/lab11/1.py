import pandas as pd
from datetime import datetime

print(pd.Timestamp('2012-01-15'))
print(pd.Timestamp('2023-01-01 21:20'))
print(pd.Timestamp.now())
print(pd.Timestamp('2023-03-01').date())
print(pd.Timestamp.today().date())
print(pd.Timestamp('2023-01-01 21:20').time())
print(datetime.now().time())