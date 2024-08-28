import pandas as pd
# 1
df = pd.read_csv('examples7/score.csv')
print('\n---imported score csv---\n', df)

# 2
df1 = df.dropna()
print('\n---removed record with missing value\n', df1)

# 3
df2 = df1.drop_duplicates(['Student_ID'], keep='last')
print('\n---drop duplicate based on student id and keep last---\n', df2)

# 4
# filter for Common test column
df3 = df2[(df2['Common Test'] < 100) & (df2['Common Test'] >= 0)]
# filter for Assignment column
df4 = df3[(df2['Assignment'] < 100) & (df2['Assignment'] >= 0)]
print(df4)

# 5
student_id_to_name = pd.read_csv('examples7/student.csv')
# convert a dataframe to dict
names_dict = dict(zip(student_id_to_name.Student_ID, student_id_to_name.Name))
# print(names_dict)
df4['name'] = df4['Student_ID'].map(names_dict)
df5 = df4
print(df5)

# 6
df5["Final Score"] = df5["Common Test"]*0.7 + df5["Assignment"]*0.3
print(df5)

# 7
def get_score(score):
    if score >= 85 and score <= 100:
        return 'A'
    if score >= 75 and score < 85:
        return 'B'
    if score >= 65 and score < 75:
        return 'C'
    if score >= 50 and score < 65:
        return 'D'
    return 'F'

grade_dict = {}
for index, row in df5.iterrows():
    final_score = df5.loc[index]["Final Score"]
    grade = get_score(final_score)
    student_id = df.loc[index]["Student_ID"]
    grade_dict[student_id] = grade

print(grade_dict)

df5['Grade'] = df["Student_ID"].map(grade_dict)
print(df5)

# 8
df5[['Student_ID', 'name', 'Grade']].to_csv('examples7/student_grades.csv', index=False)