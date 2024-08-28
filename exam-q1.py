import statistics as s
import random

# 1 (a)
def number_statistics(num_list):
    smallest = min(num_list)
    largest = max(num_list)
    mean = s.mean(num_list)
    std = s.stdev(num_list)
    return smallest, largest, mean, std

result = number_statistics([1, 3, 5, 8, 10])
print(result)

# 1 (b)
def get_unique_random_integers():
    num_list = random.sample(range(0, 100), 10)
    return num_list

result = get_unique_random_integers()
print(result)

import numpy as np

areas = np.array(['North', 'East', 'South', 'West', 'Central'])
cases = np.array([
    [1, 2, 5, 4],
    [5, 6, 3, 8],
    [6, 2, 3, 6],
    [3, 3, 4, 2],
    [2, 2, 5, 4],
])

# 2 (i)
print(cases[areas == 'East'])

# 2 (ii)
print(cases[:1, :1])

# 2(iii)
print(cases.sum() / 5)

# 2(iv)
print(cases.sum(axis=1))

# 2(v)
print(np.average(cases, axis=1))
print(np.average(cases, axis=0))

# 2(vi)
north_cases = cases[areas == 'North']
print(north_cases.max())

# 2(vii)
total_cases = cases.sum(axis=1)
print(areas[total_cases == total_cases.max()])

# 2(viii)
total = cases.sum()
area_total = cases.sum(axis=1)
area_percentage = area_total / total * 100
print(area_percentage)

zone_total = cases.sum(axis=0)
zone_percentage = zone_total / total * 100
print(zone_percentage)


import pandas as pd
students = [150, 160, 450]
halls = ["Hall1", "Hall2", "Hall3"]

# Question No.3(a)(i)
studentsSeries = pd.Series(students, index=halls)
print(studentsSeries)

# Question No.3(a)(ii)
hall2_studen_no = studentsSeries["Hall2"]
print(hall2_studen_no)

# Question No.3(a)(iii)
studentsSeries["Hall3"] = studentsSeries["Hall3"] - 12
print(studentsSeries)

# Question No.3(a)(iv)
print(studentsSeries.sum())

# Question No.3(a)(v)
print(studentsSeries[studentsSeries > 200])

# Question No.3(b)(i)
hall1 = [150, 150]
hall2 = [60, 100]
hall3 = [250, 200]

student_df = pd.DataFrame({
    "Hall1": hall1,
    "Hall2": hall2,
    "Hall3": hall3
}, index=['male', 'female'])
print(student_df)

# Question No.3(b)(ii)
print(student_df.sum())

# Question No.3(b)(iii)
male_total = student_df.loc['male'].sum()
print(male_total)
female_total = student_df.loc['female'].sum()
diff = male_total - female_total
print(diff)

# Question No.3(b)(iv)
female_student = student_df.loc['female']
result = female_student[female_student > 180]
print(result)


import pandas as pd

# Question No.4(a)
products = pd.read_csv('data/products.csv')
products = products.dropna()
products = products[products['Quantity'] <= 5]
print(products)

# Question No.4(b)
import pandas as pd
import json
json_obj = """
    {
        "name": "shops",
        "area": ["north", "east", "south", "west", "central"],
        "data": [
            {"area": "north", "number": 5},
            {"area": "east", "number": 4},
            {"area": "south", "number":3},
            {"area": "west", "number":6},
            {"area": "central", "number":10}
        ]
    }
"""

# Question No.4(b)(i)
shops_json = json.loads(json_obj)
print(shops_json)

# Question No.4(b)(ii)
shops = pd.DataFrame(shops_json["data"])
print(shops)

# Question No.4(b)(iii)
import sqlite3

query = """
    CREATE TABLE SHOPS
    (
        area VARCHAR(50),
        numbers INTEGER
    )
"""

con = sqlite3.connect('shops_data.sqlite')
con.execute(query)
con.commit()

# Question No.4(b)(iv)
stmt = "INSERT INTO SHOPS VALUES(?,?)"
con.executemany(stmt, shops.to_records(index=False).tolist())
con.commit()

# Question No.4(b)(v)
cursor = con.execute("SELECT * FROM SHOPS")
data = cursor.fetchall()
for row in data:
    print(row)


