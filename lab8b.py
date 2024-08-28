# LAB 8-B
import pandas as pd

# a-i
parents = [15, 16, 13]
parentsSeries = pd.Series(parents, index=['Bukit Timah', 'Jurong', 'Clementi'])
print(parentsSeries)

# a-ii
print(parentsSeries['Jurong'])

# a-iii
parentsSeries['Jurong'] = 17
print(parentsSeries)

# a-iv
print(parentsSeries.sum())

# b-i
columns = ['kindergarten', 'timing', 'num_of_parent']
timing = ['AM', 'PM'] * 3
parents = [7, 8, 8, 8, 7, 6]
kindergarten = ['Bukit Timah', 'Bukit Timah', 'Jurong', 'Jurong', 'Clementi', 'Clementi']
volunteer_dict = {
    'kindergarten': kindergarten,
    'timing': timing,
    'num_of_parent': parents
}
volunteer = pd.DataFrame(volunteer_dict)
print(volunteer)

# b-ii
volunteer1 = volunteer[['kindergarten', 'timing']]
num_of_parent = volunteer['num_of_parent']
print(volunteer1[(num_of_parent < 7)])

# b-iii
print(volunteer[(volunteer['timing'] == 'PM')])

# b-iv
am_volunteers = volunteer[volunteer['timing'] == 'AM']['num_of_parent'].sum()
print(am_volunteers)
pm_volunteers = volunteer[volunteer['timing'] == 'PM']['num_of_parent'].sum()
print(pm_volunteers)