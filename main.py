import pandas as pd
pd.set_option('max_colwidth', 600)
pd.set_option('display.width', 600)
df = pd.read_csv("06.05.2020.csv", sep=' ', encoding="cp1251")
len(df.index)
print(df.head(10))
