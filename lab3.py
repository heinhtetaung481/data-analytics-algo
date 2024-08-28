import csv
import statistics as s

def read_data():
    path = "students_result.csv"
    student_data = []
    with open(path,"r") as student_file:
        reader = csv.DictReader(student_file)
        for row in reader:
            sn = row.get("student_number")
            fname = row.get("first_name")
            lname = row.get("last_name")
            score = float(row.get("score"))
            data = {"student_number":sn,"first_name":fname,"last_name":lname,"score":score}
            #round the average and stddev to 2 dec place
            student_data.append(data)
        return student_data
                
#student_data = read_data()
#for data in student_data:
    #print(data)
    
def get_basic_statistics(student_data):
    #put all the scores into a list so that we can compute the min, max etc from the standard function
    score = []
    for data in student_data:
        score.append(data["score"])
    lowest = min(score)
    highest = max(score)
    average = s.mean(score)
    stddev = s.stdev(score)
    return lowest,highest,round(average,2),round(stddev,2)

def print_student_details(data):
    print("Student Number:{0}".format(data["student_number"]))
    print("First Name:{0}".format(data["first_name"]))
    print("Last Name:{0}".format(data["last_name"]))
    print("Score:{0}".format(data["score"]))
    
def print_students_with_highest_score(student_data,highest_score):
    print("Highest Score students")
    for data in student_data:
        if(data["score"]==highest_score):
            print_student_details(data)

def students_failed(student_data):
    print("Percentage and no of students failed")
    students_failed = []
    for data in student_data:
        if(data["score"] < 50):
            students_failed.append(data)
    no_of_student_failed = len(students_failed)
    no_of_total_student = len(student_data)
    percentage_failed = no_of_student_failed / no_of_total_student * 100
    print("No of Students Failed: ", no_of_student_failed)
    print("Percentage Failed: ", round(percentage_failed, 2), "%")
    for student in students_failed:
        print_student_details(student)
        print("Status: Failed")

def students_below_average(student_data):
    print("Percentage and no of students below average")
    students_below_average = []
    average = get_basic_statistics(student_data)[2]
    print(average)
    for data in student_data:
        if(data["score"] < average):
            students_below_average.append(data)
    no_of_student_below_average = len(students_below_average)
    no_of_total_student = len(student_data)
    percentage_below_average = no_of_student_below_average / no_of_total_student * 100
    print("No of Students Below Average: ", no_of_student_below_average)
    print("Percentage below average: ", round(percentage_below_average, 2), "%")
    for student in students_below_average:
        print_student_details(student)
        print("Status: below average")
            
student_data = read_data()
lowest,highest,average,stddev = get_basic_statistics(student_data)
print("Student Result Report")
print("Highest:{0}".format(highest))
print("Lowest:{0}".format(lowest))
print("Average:{0}".format(average))
print("Std dev:{0}".format(stddev))
print()
print_students_with_highest_score(student_data,highest)
students_failed(student_data)
students_below_average(student_data)