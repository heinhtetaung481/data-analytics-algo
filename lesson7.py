import pandas as pd

df = pd.read_csv('examples7/ex1.csv')
df = df.dropna()
print('\n---removed rows with na---\n', df)

df = pd.read_csv('examples7/ex2.csv')
print('\n---original ex2---\n', df)

df = df.dropna(how="all")
print('\n---removed rows with all na value---\n', df)

df = pd.read_csv('examples7/ex3.csv')
print('\n---ex3 original values---\n')

df = df.dropna(how="all", axis=1)
print('\n---removed columns with all na value---\n', df)

df = pd.read_csv("examples7/ex3.csv")
print(df)

df1 = df.dropna(thresh=4, axis=1)
print(df1)

df = pd.read_csv('examples7/ex3.csv')
print(df)
df1 = df.fillna(0)
print(df1)
df2 = df.fillna(1)
print(df2)

# fill missing data with previous row value
df3 = df.fillna(method='ffill')
print(df3)

df4 = df.fillna(method='ffill', axis=1)
print(df4)

df5 = df.fillna({"a": 1, "b": 2, "c": 3, "d": 4,"message": "hello"})
print(df5)

df6 = df[["a", "b", "c", "d"]]
print('\nmean value with index\n', df6.mean()['a'])

df7 = df.fillna(df6.mean())
print(df7)

means = df6.mean(axis=1)
print(means)

for k in means.keys():
    df.loc[k] = df.loc[k].fillna(means[k])

print(df)

df = pd.read_csv('examples7/ex4.csv')
print(df.duplicated())

df1 = df.drop_duplicates()
print('\ndefault drop duplicates\n', df1)

# drop duplicates with column 

df1 = df.drop_duplicates(['message'])
print('\ncolumn name drop duplicates\n', df1)

df1 = df.drop_duplicates(['message'], keep='last')
print('\ncolumn name drop duplicates kee last\n', df1)

# transform column using dict
df = pd.read_csv('examples7/ex5.csv')
message_to_code = {
    "hello": "code1",
    "world": "code2",
    "foo1": "code3",
    "foo2": "code4",
    "foo3": "code5"
}
df["code"] = df["message"].map(message_to_code)
print(df)