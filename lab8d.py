# LAB 8-d

import pandas as pd

# 1
attendance = pd.read_csv('data/attendance.csv')
print(attendance)

# 2
attendance = attendance.dropna()
print(attendance)

# 3
attendance = attendance.drop_duplicates(['Student_ID'], keep='last')
print(attendance)

# 4
attendance = attendance[attendance['Attendance_days'] <= 260]
print(attendance)

# 5
student = pd.read_csv('data/student.csv')
print(student)
student_id_to_name = dict(zip(student.Student_ID, student.Name))
attendance['Name'] = attendance['Student_ID'].map(student_id_to_name)
print(attendance)

# 6
attendance['percentage'] = round(attendance['Attendance_days']/260 * 100, 2)
print(attendance)

# 7
def attendance_grade(attendance):
    data = {}
    for index, row in attendance.iterrows():
        if row['percentage'] >= 80:
            data[row['Student_ID']] = 'Excellent'
        elif row['percentage'] >= 70:
            data[row['Student_ID']] = 'Good'
        elif row['percentage'] >= 60:
            data[row['Student_ID']] = 'Fair'
        elif row['percentage'] < 60:
            data[row['Student_ID']] = 'Poor'

    return data

student_id_to_grade = attendance_grade(attendance)
print(student_id_to_grade)

attendance['Grade'] = attendance['Student_ID'].map(student_id_to_grade)
print(attendance)

# 8
attendance[['Student_ID', 'Name', 'Attendance_days', 'Grade']].to_csv('data/student_grades.csv' ,index=False)