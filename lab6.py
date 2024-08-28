import json
import pandas as pd
import sqlite3

string_json = """
{
    "name": "dengue cases",
    "area": ["north", "east", "south", "west"],
    "data": [
        {"area": "north", "cases": 45},
        {"area": "east", "cases": 64},
        {"area": "south", "cases": 34},
        {"area": "west", "cases": 33}
    ]
}
"""

# a
res_json = json.loads(string_json)
print('\n---String of JSON---\n', res_json)

# b
dengue_cases = pd.DataFrame(res_json['data'])
print('\n---Dengue Cases DF---\n', dengue_cases)

# c
query = """
    CREATE TABLE DENGUE_CASES
    (area VARCHAR(50),
    cases INTEGER)
"""

con = sqlite3.connect("dengue_cases.sqlite")
# con.execute(query)
# con.commit()

# d
stmt = "INSERT INTO DENGUE_CASES VALUES(?,?)"
con.executemany(stmt, dengue_cases.to_records(index=False).tolist())
con.commit()

# e
cursor = con.execute("SELECT * FROM DENGUE_CASES")
rows = cursor.fetchall()
print('\n---Fetch data from Database---\n')
for row in rows:
    print(row)