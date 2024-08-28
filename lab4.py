import numpy as np

hospital = np.array(['KKH', 'TTH', 'SCH', 'CCH'])
beds = np.array([[20, 30, 50, 10],
                 [10, 100, 200, 30],
                 [30, 120, 220, 30],
                 [0, 220, 320, 40]])
# a(i)
print('Beds in SCH Hodpital', beds[hospital == "SCH"])
# a(ii)
print('All Emergency Ward Information', beds[:, 3:4])
# a(iii)
print('average no of beds for each ward type', beds.mean(axis=0))
# a(iv)
print('hospital with highest no of emergency ward bed', hospital[beds[:, -1] == beds[:, -1].max()])
# a(v)
day1_admission = np.array([4, 3, 2, 14])
day2_admission = np.array([8, 3, 4, 10])
allday_admission = np.array([day1_admission, day2_admission])
print('average admission for ward a', allday_admission.mean(axis=0)[0])

# b
hospitals = np.array(['CCH', 'SCH', 'TTH'])
admissions = np.array([151, 262, 253])

print('sorted hospital according to admissions', np.flip(hospitals[admissions.argsort()]))

# c
symptons = np.array(['flu', 'chest pain', 'fever', 'cough', 'headache', 'headache', 'fever'])
unique_symptons = np.unique(symptons)
print('unique symptons', unique_symptons)
print('length of unique symptoms', len(unique_symptons))

# d
patient1 = np.array(["flu", 'fever', 'headache'])
patient2 = np.array(["flu", 'chest pain', 'fever'])

diff1 = np.setdiff1d(patient1, patient2)
diff2 = np.setdiff1d(patient2, patient1)
diff = np.concatenate((diff1, diff2))
print('symptoms not common between patients', diff)

# e
patient1 = np.array(["flu", 'fever', 'headache'])
patient2 = np.array(["flu", 'chest pain', 'fever'])

unique_symptons = np.union1d(patient1, patient2)
print('unique symptoms for patients', unique_symptons)