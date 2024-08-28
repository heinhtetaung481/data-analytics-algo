import pandas as pd
import json

df = pd.read_csv('examples6/ex1.csv')
print(df)

df = pd.read_table('examples6/ex2.csv', sep = '|')
print(df)

df = pd.read_csv('examples6/ex3.csv', header=None)
print(df)

column_names = ['a', 'b', 'c', 'd', 'Message']
df = pd.read_csv('examples6/ex3.csv', names = column_names, index_col="Message")
print(df)

df = pd.read_csv('examples6/ex1.csv', skiprows=[2, 3])
df.to_csv('examples6/out.csv', index=False)
print(df)

df = pd.read_csv('examples6/ex4.csv')
print(df)

json_string="""
{
    "students":[
        {
            "firstName":"John",
            "lastName":"Tan",
            "age":21
        },
        {
            "firstName":"Mary", 
            "lastName":"Lim",
            "age":19
        },
        {
            "firstName":"Peter", 
            "lastName":"Chan",
            "age":20
        }
    ]
}
"""

data = json.loads(json_string)
print(data)

df = pd.DataFrame(data["students"], columns=['firstName', 'lastName'])
print(df)

url="https://data.gov.sg/api/action/datastore_search?resource_id=4ad866a7-c43a-4645-87fd-fc961c9de78a"


# import urllib.request
# class AppURLopener(urllib.request.FancyURLopener):
#     version = "Mozilla/5.0"

# opener = AppURLopener()
# response = opener.open(url)
# data = json.loads(response.read())
# print(data.keys())
# print(data["result"])
# df = pd.DataFrame(data["result"]["records"])
# print(df)

import requests
res = requests.get(url)
df = pd.DataFrame(res.json()['result']['records'])
print('-----requests-------\n', df)


excel_data = pd.ExcelFile('examples6/ex1.xlsx')
sheet1_data = pd.read_excel(excel_data, "Sheet1")
print(sheet1_data)

data = {
    "clinic": [
        "A",
        "A",
        "A",
        "B",
        "B",
        "B"
    ],
    "year": [2017, 2018, 2019] * 2,
    "visits": [1054, 1089, 1342, 805, 1025, 1320]
}
dfClinics = pd.DataFrame(data)
print(dfClinics)
dfClinics.to_excel('examples6/clinics.xlsx', index=False)

import sqlite3

query = """
    CREATE TABLE patient
    (first_name VARCHAR(50),
     last_name VARCHAR(50),
     age INTEGER,
     height REAL,
     weight REAL
    )
"""

con = sqlite3.connect("patient_data.sqlite")
# con.execute(query)
# con.commit()

data = [
    ("John", "Lim", 20, 1.73, 65.7),
    ("Peter", "Tan", 21, 1.83, 87.9)
]
# con = sqlite3.connect("patient_data.sqlite")
stmt = "INSERT INTO patient VALUES(?,?,?,?,?)"
con.executemany(stmt, data)
con.commit()

cursor = con.execute("SELECT * FROM patient")
rows = cursor.fetchall()
for row in rows:
    print(row)