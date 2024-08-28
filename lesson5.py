import pandas as pd

pdSeries1 = pd.Series([3, 2, 1, 2])
print(pdSeries1.values)

data_list = [6, 3, 4, -5, 2]
index_list = ["d", "b", "a", "e", "c"]
# pdSeries2 = pd.Series(data_list)
# pdSeries2.index = index_list

pdSeries2 = pd.Series(data_list, index=index_list)

print(pdSeries2.index)

# s10
print('default index', pdSeries2[0])
print('assigned index', pdSeries2["d"])

# p11
print('slicing', pdSeries2[2:4])
# p12
print('slice using list of index', pdSeries2[[1, 3]])
# 13
print('slice using list of index named', pdSeries2[['a', 'b', 'c']])
# s14
print('fetch using conditions/boolean indexing', pdSeries2<3)
print('fetch using conditions/boolean indexing', pdSeries2[pdSeries2<3])
# s15
pdSeries2[1] = 10
print(pdSeries2)

pdSeries2["a"] = 12
print(pdSeries2)

pdSeries2[2:5] = 14
print('slice update', pdSeries2)

# s16
print('math ops plus', pdSeries2+2)
print('math ops minus', pdSeries2-2)
print('math ops multiply', pdSeries2*2)
print('math ops division', pdSeries2/2)

# s17
data_list2 = [8, 2, -3, 9, 2, 3]
index_list2 = ['a', 'e', 'd', 'b', 'c', 'f']
pdSeries3 = pd.Series(data_list2, index=index_list2)
print('adding two series with same index', pdSeries2 + pdSeries3)

# s18
print('two series math ops plus', pdSeries2+pdSeries3)
print('two series math ops minus', pdSeries2-pdSeries3)
print('two series math ops multiply', pdSeries2*pdSeries3)
print('two series math ops division', pdSeries2/pdSeries3)

# s20
# two series must have the exact same index
data_list = [2, 6, 7, 3, 2]
index_list = ['d', 'b', 'a', 'e', 'c']

pdSeries4 = pd.Series(data_list, index=index_list)
print('two series comparison', pdSeries2<pdSeries4)

# s21
scores = {'Ada': 85, 'Charles': 62, 'Bob': 72}
pdSeries5 = pd.Series(scores)
print('create series by dict', pdSeries5)

# s22
print('default sort index', pdSeries5.sort_index())
print('descending sort index', pdSeries5.sort_index(ascending=False))
print('default sort values', pdSeries5.sort_values())
print('descending sort values', pdSeries5.sort_values(ascending=False))

# s23
scores = {'Ada': 85, 'Charles': 62, 'Bob': 72}
index_order = ['Ada', 'Bob', 'Daniel']
pdSeries6 = pd.Series(scores, index=index_order)
print('pass index to dict series', pdSeries6)

# s24
print('isnull', pdSeries6.isnull())
print('isnull', pd.isnull(pdSeries6))

print('notnull', pdSeries6.notnull())
print('notnull', pd.notnull(pdSeries6))

# s25
pdSeries6.name = 'Exam Score'
pdSeries6.index.name = 'Student Name'
print('with names', pdSeries6)

# s26
pdSeries6 = pdSeries6.drop('Daniel')
print('remove item', pdSeries6)

# s28
print('sum', pdSeries6.sum())
print('mean', pdSeries6.mean())
print('std', pdSeries6.std())
print('describe', pdSeries6.describe())

# s31
# DataFrame
data = {'clinic': ['A', 'A', 'A', 'B', 'B', 'B'],
        'year': [2017, 2018, 2019] * 2,
        'visits': [1054, 1089, 1342, 805, 1025, 1320]
        }
dfClinics = pd.DataFrame(data)
print('DataFrame \n', dfClinics)

# s32
print('head \n', dfClinics.head())

# s33
dfClinics = pd.DataFrame(data, columns=['year', 'visits'])
print('pass desired columns list \n', dfClinics)

# s34
dfClinics = pd.DataFrame(data, columns=['year','clinic', 'visits', 'mild', 'serious'])
print('pass desired columns list with non-existing column name \n', dfClinics)

# s35
dfClinics = pd.DataFrame(data, 
                columns=['year', 'clinic', 'visits'],
                index=['A1', 'A2', 'A3', 'B1', 'B2', 'B3'])
print('pass desired columns list and index \n', dfClinics)

# s36
print('retrieve data from data frame using column name as index \n', dfClinics['clinic'])
print('retrieve data from data frame using column name as index \n', dfClinics.year)

# s37
print('retrieve row using loc \n', dfClinics.loc['A2'])

# s38
mild_cases = [502, 620, 928, 670, 802, 1025]
dfClinics["mild"] = mild_cases
print('assign new values to column \n', dfClinics)

# 39
dfClinics['serious'] = dfClinics.visits - dfClinics.mild
print('compute new columns using existing two columns \n', dfClinics)

# s40
reference = [120, 321, 392, 20, 42, 146]
dfClinics['reference'] = reference
print('add new column \n', dfClinics)

# s41
reference = pd.Series([20, 42, 146, 120, 321, 392], index=['B1', 'B2', 'B3', 'A1', 'A2', 'A3'])
dfClinics['reference'] = reference
print('assign new column by index \n', dfClinics)
# if the index is missing it will appear as NaN for the rest values/index

# s43
index = ['B1', 'B2', 'B3', 'A1', 'A2', 'A3', 'C']
dfClinics = dfClinics.reindex(index)
print('reindex\n', dfClinics)

# s44
column = ['year', 'clinic', 'mild', 'serious', 'visits', 'reference']
dfClinics = dfClinics.reindex(columns=column)
print('reindex columns\n', dfClinics)

# s45
column = ['year', 'clinic', 'mild', 'serious', 'visits', 'reference', 'fatality']
dfClinics = dfClinics.reindex(columns=column, fill_value=0)
print('reindex and new column with default value\n', dfClinics)

# 46
dfClinics = dfClinics.drop(['reference', 'fatality'], axis=1)
print('drop column by axis=1\n', dfClinics)
# dfClinics = dfClinics.drop(['reference', 'fatality'], axis='columns')
# print('drop column by axis=columns\n', dfClinics)

# 47
dfClinics = dfClinics.drop(['B3', 'C'])
print('drop row by index\n', dfClinics)

# 48
print('access column using column name\n', dfClinics['year'])
print('access column using multiple column names\n', dfClinics[['year', 'mild']])

# s49
# same as the previous one s37

# s50
print('access row using slice index\n', dfClinics[1:3])

# 52
print('filtering.....')
print(dfClinics.mild > 800)
print('boolean index filtering\n', dfClinics[dfClinics.mild > 800])

# s54
visits_data = dfClinics[['mild', 'serious', 'visits']]
print('df sum \n', visits_data.sum())

# s55
print('df mean \n', visits_data.mean())

# s56
print('df std \n', visits_data.std())

# s57
print('df describe \n', visits_data.describe())

# s58
print('df sum by row\n', dfClinics[['mild', 'serious']].sum(axis=1))

# s59
data = {
    "clinic": ['A', 'A', 'A', 'B', 'B', 'B'],
    'year': [2017, 2018, 2019] * 2,
    'mild': [502, None, 928, None, 802, 1025],
    'serious': [552, 469, 414, 135, 223, 295]
}
dfClinics = pd.DataFrame(data)
print(dfClinics)

# s60
cases = dfClinics[['mild', 'serious']]
print('sum with NaN\n', cases.sum(axis=1))

# 61
print('mean with NaN\n', cases.mean())

# s62
print('mean with NaN with skip false\n', cases.mean(skipna=False))

# 63
print('mean with NaN by row\n', cases.mean(axis=1))

# s64
print('mean with NaN with skip false by row\n', cases.mean(skipna=False, axis=1))

# s66
rental = [400, 420, 450, 450, 500]
dist_station = [450, 420, 400, 350, 300]
dist_market = [350, 320, 400, 230, 400]

column_header = ["Rental", "Dist from station", "Dist from market"]

data = {
    "rental": rental,
    "dist_from_station": dist_station,
    "dist_from_market": dist_market
}

dfHouseRental = pd.DataFrame(data)
print(dfHouseRental)

# s67
print('correlation between rental and dist from station\n',
    dfHouseRental.rental.corr(dfHouseRental.dist_from_station))
print('correlation between rental and dist from market\n',
    dfHouseRental.rental.corr(dfHouseRental.dist_from_market))

# 68
print('correlation between all columns\n', dfHouseRental.corr())
print('covariance\n', dfHouseRental.cov())
