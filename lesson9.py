import pandas as pd

df1 = pd.read_csv('lesson9data/data1.csv')
df2 = pd.read_csv('lesson9data/data3.csv')

df3 = pd.merge(df1, df2, how="right")
df4 = pd.merge(df1, df2, how="outer")
print(df4)

df2 = pd.read_csv('lesson9data/data2.csv', index_col="key")

df3 = pd.merge(df1, df2, left_on="key", right_index=True)
print(df3)

df1 = pd.read_csv('lesson9data/data1.csv', index_col="key")
df2 = pd.read_csv('lesson9data/data2.csv')

df3 = pd.merge(df1, df2, left_index=True, right_on="key")
print(df3)



