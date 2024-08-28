# import pandas as pd

# # testing pandas package
# panda_test_var = pd.unique(pd.Series([2, 1, 3, 3]))
# print(panda_test_var)

# # following the lesson from here
# # string concat
# name1 = "John"
# family_name1 = "Doe"
# name2 = "Jane"

# print("Hello I am {0} {1}".format(name1, family_name1))
# print(f"Hello I am {name1} {family_name1}")
# print("{0:10} {1}".format("Name", "Family Name"))
# print("{0:10} {1}".format(name1, family_name1))
# print("{0:10} {1}".format(name2, family_name1))
# print("{0:10} {1}".format(name1, family_name1))

# # lesson abt int
# num1 = 12.6
# num2 = 13.3
# total = num1 + num2

# print(total)

# # lesson for input
# text = input("Enter some text:")
# print(text)

# # multiple inputs
# num3 = input("Enter num1:")
# num3 = int(num3)
# num4 = input("Enter num2:")
# num4 = int(num4)
# print(num3 + num4)

# # decimal inputs
# num5 = input("Enter float1:")
# num5 = float(num5)
# num6 = input("Enter float2:")
# num6 = float(num6)
# total = num5 + num6
# diff = num5 - num6
# product = num5 * num6
# division = num5 / num6
# power = num5 ** num6
# sq_root = num5 ** 0.5

# diff = round(diff, 2)

# print(f"total: {total}")
# print(f"diff: {diff}")
# print(f"product: {product}")
# print(f"division: {division}")
# print(f"total: {total}")
# print(f"Exp: {power}")
# print(f"Sq root of {num5} is {sq_root}")

# conditional statement
# num1 = int(input('Enter int:'))
# num2 = int(input('Enter int:'))
# num3 = int(input('Enter int:'))

# max_n = num1
# if(num2 > max_n):
#     max_n = num2

# if(num3 > max_n):
#     max_n = num3

# print(f'Max of {num1}, {num2}, {num3} is {max_n}')

# if(n1 == 5):
#     print('yes it is 5')

# num1 = int(input("enter num:"))

# if(num1>0):
#     print('positive')
# elif(num1<0):
#     print('negative')
# else:
#     print('it is zero')

# marks = int(input('enter your marks: '))

# if(marks >= 85):
#     grade = "A"
# elif(marks >= 75):
#     grade = "B"
# elif(marks >= 65):
#     grade = "C"
# elif(marks >= 50):
#     grade = "D"
# else:
#     grade = "F"

# print(f"Marks: {marks} Grade: {grade}")

# n1 = 5

# if(n1 > 8 and n1<10):
#     print("n1 is within range")
# else:
#     print('n1 is not within range')

# if(n1 > 1 or n1 < 5):
#     print("n1 is within range")
# else:
#     print('n1 is not within range')

# temperature lab 3

temp = float(input('enter temp: '))

if(temp >= 100):
    state = "gas"
elif(temp < 100 and temp > 0):
    state = "liquid"
else:
    state = "solid"

print(f"the state of water at {temp} is {state}")

amount = float(input('enter amount: '))
gender = input('input gender: ')

if(amount >= 100):
    if(gender == "m"):
        gift = "Shaver"
    else:
        gift = "Hand Cream"
else:
    print('thank you for shopping')


age = int(input("enter age: "))
gender = input('enter gender: ')

if((gender == 'm' and age >= 15) or (gender == 'f' and age >= 17)):
    print('go inside okay')
else:
    print('not allowed ot enter')





