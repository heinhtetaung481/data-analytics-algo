# LAB 8-A

import numpy as np

kindergarten = np.array(['Bukit Timah', 'Clementi', 'Jurong'])
student_level = np.array([
    [26, 33, 22],
    [18, 10, 14],
    [30, 32, 31]
])

# a-i
clementi = student_level[kindergarten == 'Clementi']
print(clementi)

# a-ii
print((student_level[:,1]))

# a-iii
print(student_level.mean(axis=0))

# a-iv
max_enrollment = student_level[:, 0].max()
max_enrollment_place = kindergarten[student_level[:, 0] == max_enrollment]
print('max', max_enrollment_place)
# print(student_level[:,1])

# a-v
absentee1 = np.array([18, 15, 19])
absentee2 = np.array([15, 13, 14])
absentee3 = np.array([19, 14, 18])

a=(absentee1 + absentee2 + absentee3)/3 
print(a) 
print(a[0])

# b
total_enroll = student_level.sum(axis=1)
print('total', total_enroll)
total_enroll_argsort = total_enroll.argsort()
print('argsort', total_enroll_argsort)
kindergarten_enrollment_ranking_asc = kindergarten[total_enroll_argsort]
kindergarten_enrollment_ranking_desc = np.flip(kindergarten_enrollment_ranking_asc)
print(kindergarten_enrollment_ranking_desc)

# c

student1 = np.array(["flu", "fever"])
student2 = np.array(["food poisoning", "diarrhea"])
student3 = np.array(["parental leaves"])
student4 = np.array(["fever"])
student5 = np.array(["chickenpox", "fever"])

student = np.concatenate([student1, student2, student3, student4, student5])
unique_reasons = np.unique(student)
print(unique_reasons)
print(len(unique_reasons))