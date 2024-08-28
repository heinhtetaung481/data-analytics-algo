import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

# x = range(10)
# plt.plot(x)
# plt.show()

# data = np.random.randn(50)
# print(data)
# plt.plot(data, color="b", marker="o", linestyle="-")
# plt.show()

# dataX = np.random.randn(30)
# dataY = np.random.randn(30)
# plt.scatter(dataX, dataY, color="b", marker="x")
# plt.show()

# histogram
# x is bin and y is frequency
# data = np.random.randn(30)
# plt.hist(data, bins=20, color="k", alpha=0.3)
# plt.show()

# fig = plt.figure()
# # create subplots in a 2*2 figure
# subplot1 = fig.add_subplot(2, 2, 1)
# plt.title('test1')
# subplot2 = fig.add_subplot(2, 2, 2)
# plt.title('test 2')
# subplot3 = fig.add_subplot(2, 2, 3)
# plt.title('test 3')
# data = np.random.randn(50)
# subplot1.plot(data, color="k", marker="*", linestyle="-")

# dataX = np.random.randn(30)
# dataY = np.random.randn(30)
# subplot2.scatter(dataX, dataY, color="r", marker="x")

# data = np.random.randn(30)
# subplot3.hist(data, bins=20, color="b")

# plt.show()


# data = np.random.randn(30)
# plt.plot(data, color='k',marker="*",label='data label')
# plt.legend(loc='best')
# plt.show()

# data1 = np.random.randn(30)
# plt.plot(data1, color="k", label="data 1")
# data2 = np.random.randn(30)
# plt.plot(data2, color="b", label="data 2")

fig = plt.figure()
data = np.random.randn(1000)
subplot = fig.add_subplot(2,2,1)
subplot.plot(data)
subplot = fig.add_subplot(2,2,2)
subplot.plot(data)

subplot.set_xticks([0, 250, 500, 750, 1000])
subplot.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
                          rotation=30, fontsize='small')
#note 0 map to one, 250 map to two and so on

subplot.set_title("A matplot")
subplot.set_xlabel("Data X")
subplot.set_ylabel("Data Y")

plt.show()
plt.savefig('figpath.pdf')

# data=np.random.randn(10)
# s = pd.Series(data)
# s.plot()
# plt.show()

# df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
#                   columns=['A', 'B', 'C', 'D'],
#                   index=np.arange(0, 100, 10))
# print(df)
# df.plot()
# plt.show()

# print(np.random.randn(10, 4).cumsum(0))

# np.random.seed(12348)
# df = pd.DataFrame(np.random.rand(6, 4),
#                   index=['one', 'two', 'three', 'four', 'five', 'six'],
#                   columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
# df.plot.barh(stacked=True, alpha=0.5)
# plt.show()

# data = pd.read_csv('data10/restaurants.csv')
# party_counts = pd.crosstab(data['day'], data['size'])
# print(party_counts)
# print()
# party_counts = party_counts.loc[:, 2:5]
# print(party_counts)

# sum_day = party_counts.sum(1)
# print(sum_day)

# percent = party_counts.div(sum_day, axis=0) * 100
# print(percent)
# percent.plot.bar()
# plt.show()

# data = pd.read_csv('data10/restaurants.csv')
# data['tip_pct'] = data['tip'] / (data['total_bill'] - data['tip']) * 100
# data['tip_pct'].plot.hist(bins=50)
# plt.show()

# data = pd.read_csv('data10/restaurants.csv')
# data['tip_pct'] = data['tip'] / (data['total_bill'] - data['tip']) * 100
# data['tip_pct'].plot.density()
# plt.show()


# data = pd.read_csv('data10/restaurants.csv')
# data['tip_pct'] = data['tip'] / (data['total_bill'] - data['tip'])

# sns.barplot(x="tip_pct", y='day', data=data, orient='h')
# plt.show()

# sns.barplot(x="tip_pct", y="day", hue="time", data=data, orient='h')
# plt.show()

# comp1 = np.random.normal(0, 1, size=200)
# comp2 = np.random.normal(10, 2, size=200)
# values = pd.Series(np.concatenate([comp1, comp2]))
# sns.distplot(values, bins=100, color="k")
# plt.show()

# macro = pd.read_csv('data10/macrodata.csv')
# data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
# trans_data = np.log(data).diff().dropna()
# print(trans_data.head())

# sns.regplot(x="m1",y="unemp",data=trans_data)
# plt.title('Changes in log %s versus log %s' % ('m1', 'unemp'))
# plt.show()

# data['tip_pct'] = data[data.tip_pct < 1]
# sns.catplot(x='day', y='tip_pct', hue="time", col="smoker", kind="bar", data = data)
# plt.show()

# sns.catplot(x='tip_pct', y="day", kind="box", data=data)
# plt.show()



