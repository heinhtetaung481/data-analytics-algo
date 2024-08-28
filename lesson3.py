# path = "example.txt"

# # with open(path, "w") as example_file:
# #     example_file.write("Hi !")
# #     example_file.write("This is to write to a text file\n")
# #     example_file.write("This is second line to write to a text file\n")

# with open(path) as file:
#     for line in file:
#         print(line, end="")

import csv
import statistics as s

path = "students_result.csv"

# r1 = {"student_number" : "1111", "first_name": "John", "last_name": "Smith", "score": 90}
# r2 = {"student_number" : "2222", "first_name": "Peter", "last_name": "Leee", "score": 80}
# r3 = {"student_number" : "3333", "first_name": "Mary", "last_name": "Tan", "score": 70}

# with open(path, "w") as file:
#     field_name = ["student_number", "first_name", "last_name", "score"]
#     writer = csv.DictWriter(file, fieldnames = field_name)
#     writer.writeheader()
#     writer.writerow(r1)
#     writer.writerow(r2)
#     writer.writerow(r3)

def read_data():
    path = 'students_result.csv'
    student_data = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            sn = row.get("student_number")
            fname = row.get('first_name')
            lname = row.get('last_name')
            score = row.get('score')
            data = {"student_number": sn, "first_name": fname, "last_name": lname, "score": score}
            student_data.append(data)
        return student_data

def get_basic_statistics(student_data):
    score=[]
    for data in student_data:
        score.append(int(data["score"]))
    print(score)
    lowest = min(score)
    highest = max(score)
    average = s.mean(score)
    stddev = s.stdev(score)
    return lowest, highest, round(average, 2), round(stddev, 2)

def print_student_details(data):
    print(f"Student Number: {")
student_data = read_data()
lowest, highest, average, stddev = get_basic_statistics(student_data)

print(f"Student Report \n Highest: {highest} \n Lowest: {lowest} \n Average: {average} \n Std dev: {stddev}")