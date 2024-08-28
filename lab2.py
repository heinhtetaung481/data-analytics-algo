#1a
i=3
while(i<24):
    print(i)
    i=i+4

#1b
i=30
while(i>19):
    print(i)
    i=i-2

#2a
for i in range(12,25,3):
    print(i)
#2b
for i in range(46,25,-4):
    print(i)

# 3a
n=5
for i in range(n):
    print("A|"*n)
    
# 3b
n=5
for i in range(1,n+1):
    print("+="*i)
# 3c
for i in range(5, 0, -1):
    print("B|" * i)
    print(i)
# 3d
for i in range(5, 0, -1):
    print(":>" * i + "  " + ":P" * (6-i))

#4
n=50000
harmonic_sum = 0
for d in range(1,n+1):
    harmonic_sum+=1/d
print("harmonic_sum:{0}".format(harmonic_sum))

#5
n=200
fibo1 = 0
fibo2 = 1
print(fibo1)
print(fibo2)
for n in range(n-2):
    fibo = fibo1 + fibo2
    print(fibo)
    fibo1 = fibo2
    fibo2 = fibo

#6
nameList = ["Peter","John","Bob","Adrian"]
for name in nameList:
    print(name)
         #range(3,-1,-1)=>[3,2,1,0]
for i in range(len(nameList)-1,-1,-1):
    print(nameList[i])
for i in range(-1,-len(nameList)-1,-1):
    print(nameList[i])

#7
animals = ["fish","cat","dog","lion"]
for animal in animals:
    print(animal)
print()
for animal in animals:
    if(len(animal)==3):
        print(animal)

# 8
num_list = list(range(0, 332, 4))
total = 0
for num in num_list:
    total += num

print(total)

#9
import statistics as s
num_list = []
for i in range(5):
    num = int(input("Enter num {0}:".format(i+1)))
    num_list.append(num)
print("Largest:{0}".format(max(num_list)))
print("Lowest:{0}".format(min(num_list)))
print("Average:{0}".format(s.mean(num_list)))

#10
import statistics as s
num_list = []
i=0
while True:
    num = input("Enter num {0} or q:".format(i+1))
    i+=1
    if(num=="q"):
        break
    num = int(num)
    num_list.append(num)
print("Largest:{0}".format(max(num_list)))
print("Lowest:{0}".format(min(num_list)))
print("Average:{0}".format(s.mean(num_list)))

# 11
import statistics as s
def printPopAndStddev():
    num_list = []
    while(True):
        input_value = input("Enter a num or q to quit: ")
        if(input_value == "q"):
            # print(num_list)
            pstdev = s.pstdev(num_list)
            stdev = s.stdev(num_list)
            print(f"population stdev: {pstdev}")
            print(f"std deviation: {stdev}")
            break
        else:
            num_list.append(int(input_value))
printPopAndStddev()


#12
import math
def area_circle(radius):
    area = math.pi*radius**2
    return area

def area_triangle(base,height):
    area = 0.5*base*height
    return area

triangle_area = area_triangle(10,5) - area_triangle(3,2)
total_area = triangle_area + 2*area_circle(6)
print("Total area:{0}".format(total_area))

# 13a - b
num_list = [1, 2, 3, 4]
def number_range(num_list):
    max = 0
    min = 0
    for num in num_list:
        if num < min:
            min = num
        if num > max:
            max = num

    return max, min

max , min = number_range(num_list)

#14
import random
def dice():
    dice_text = ["one","two","three","four","five","six"]
    r = random.randint(1,6)
    return dice_text[r-1]
#test the function
for i in range(100):
    print(dice())
    
# 15
marks = {
    "John": [76, 65, 43],
    "Mary": [68, 56, 74],
    "Peter": [46, 55, 48],
}

# 15-a
marks.update({"Ada": [56, 45, 65]})

# print(marks)

# 15-b

mary_marks = marks.get("Mary")
mary_marks[2] = 87

# 15-c
marks.pop("Peter")

# 15-d
def showMarks(marks, name):
    print(f"Marks for {name}")
    print(f"Science: {marks.get(name)[2]}")
    print(f"Math: {marks.get(name)[1]}")
    print(f"Science: {marks.get(name)[0]}")

# 15-e
def showAllMarks(marks):
    print("Show all students marks")
    for name in marks.keys():
        showMarks(marks, name)

# 15-f
def studentPassedEngList(marks):
    for name in marks.keys():
        score = marks.get(name)
        if score[0] >= 50:
            print(name)

studentPassedEngList(marks)
showAllMarks(marks)
print(marks)

#16a
laptops={"acer":20,"hp":10,"toshiba":15,"apple":12}
for brand in laptops.keys():
    stock = laptops.get(brand)
    print("{0}:{1}".format(brand,stock))
#16b
print("Stock 15 or more")
for brand in laptops.keys():
    stock = laptops.get(brand)
    if(stock>=15):
        print("{0}:{1}".format(brand,stock))
#16c
total = 0
for brand in laptops.keys():
    stock = laptops.get(brand)
    total+=stock
print("Total stock:{0}".format(total))

#17
names=["Alan","Peter","Mary","John"]
ages = [17,18,19,20]
friends = {}
for i in range(len(names)):
    key = names[i]
    value = ages[i]
    friends[key] = value
print(friends)


