import pandas as pd
df = pd.read_csv("06.05.2020.csv", sep=r'\t', encoding="cp1251", engine='python')
print(df.head(10)
