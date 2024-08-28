# LAB 8-C

import pandas as pd
import json
import sqlite3

enrolment_dic = {
    "name": "enrollments",
    "area": ["Bukit Timah", "Clementi", "Jurong"],
    "data": [
        {"area": "Bukit Timah", "enrollment": 45},
        {"area": "Clementi", "enrollment": 64},
        {"area": "Jurong", "enrollment": 34}
    ]
}

# a
enrollment_string = """
    {
    "name": "enrollments",
    "area": ["Bukit Timah", "Clementi", "Jurong"],
    "data": [
        {"area": "Bukit Timah", "enrollment": 45},
        {"area": "Clementi", "enrollment": 64},
        {"area": "Jurong", "enrollment": 34}
    ]
}
"""
enrollment_json = json.loads(enrollment_string)
print(enrollment_json)

# b
enrollment = pd.DataFrame(enrollment_json['data'])
print(enrollment)

# c
query = """
    CREATE TABLE ENROLLMENT
    (area VARCHAR(50),
     enrollment INTEGER
    )
"""

con = sqlite3.connect('enrollment_data.sqlite')
con.execute(query)
con.commit()

# d
stmt = "INSERT INTO ENROLLMENT VALUES(?,?)"
con.executemany(stmt, enrollment.to_records(index=False).tolist())
con.commit()

# e
cursor = con.execute("SELECT * FROM ENROLLMENT")
data = cursor.fetchall()
for row in data:
    print(row)