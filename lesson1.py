import statistics as s
import math
num_list = [3, 5, 7, 9]
print(s.mean(num_list))
print(s.stdev(num_list))
print(s.median(num_list))

list3 = [1, "string", True, 10, "John"]

print(list(range(10, -1, -3)))

for i in range(len(num_list)):
    print(f"index {i}: {num_list[i]}")


def sum_num_list(list):
    total = 0
    for num in list:
        total += num 
    return total

print(sum_num_list(num_list))

amanda = {
    "first_name": "Amanda",
    "last_name": "Smith",
    "age": 20
    }

print(amanda.get('age', 0))
print(list(amanda.keys()))

def generate_a_pattern(n):
    for i in range(n):
        print("A|" * n)

for i in range(5):
    print("+=" * i)

for i in range(5, -1, -1):
    print(":>" * i + " " + ":P" * (5-i))

n=50000
harmonic_sum=0
for d in range(1, n+1):
    harmonic_sum += 1/d

print(harmonic_sum)

generate_a_pattern(5)

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


name_list = ["peter", 'john', 'bob', 'adrian']

for name in name_list:
    print(name)

for i in range(len(name_list)-1, -1, -1):
    print(name_list[i])

animals = ['fish', 'cat', 'dog', 'lion', 'tiger', 'mouse', 'cow']

for animal in animals:
    if (len(animal) == 3):
        print(animal)

num_list = list(range(0, 332, 4))
print(num_list)
total = 0
for num in num_list:
    total += num

print(total)

# num_list = []
# for i in range(5):
#     num = int(input("enter num:"))
#     num_list.append(num)

# print(num_list)
# max = max(num_list)
# min = min(num_list)
# average = s.mean(num_list)
# print(max)
# print(f"largest: {max}")
# print(f"flowest: {min}")
# print(f"average: {average}")

def area_circle(r):
    a = math.pi * r * r
    return a

def area_triangle(base, height):
    a = base * height / 2
    return a

triangle_area = area_triangle(10, 5) - area_triangle(3, 2)
total_area = triangle_area + 2 * area_circle(6)

print(f"total area: {total_area}")

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

print(max, min)

def create_dict(list1, list2):
    friends = {}
    for i in range(len(list1)):
        friends[list1[i]] = list2[i]
    return friends

print(create_dict(['a', 'b', 'c'], ['1', '2', '3']))