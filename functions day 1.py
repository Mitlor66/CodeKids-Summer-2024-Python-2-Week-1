"""
Functions and scope
Day 1
Timur Y
"""

print("Day 1")

# Variables: Remember a piece of information
age = 32          # Integer (whole number)
name = "Tim"      # String  (textual information)
temp = 19.7       # Float   (Decimal number)
isSunny = True    # Boolean (True or False)

coordinates = (10, 15, 11)                       # Tuple
groceries = ["Banana", "Apple", "Ham", "Bread"]  # List
students = {"Anna": 27, "Sarah": 47, "John": 24} # Dictionary


# Functions: Do something (an action)

print("I am a function that displays something on screen")

# Let's create our own function that will ask the user for their grade
def get_grade():
    grade = input("How much did you get at your previous test? ")
    grade = int(grade)

    if grade > 15:
        print("That's great!")
    elif grade > 10:
        print("That's okay but could do better")
    else:
        print("Must revise more next time")


# Let's now call the function we just created
get_grade()


# Between a function brackets, we can provide parameters/arguments/inputs
# That allows the function to have some information to work with
def add(a, b):
    print(f"{a} + {b} = {a+b}")

add(7, 2)
add(9, -5)

# Exercise 1:
# Let's create a function called fah_to_cel(temp) that will convert the
# argument temp from farhenheit to celsius using the formula:
# (temp - 32) * (5/9)

def fah_to_cel(temp):
    celsius = (temp - 32) * (5/9)
    print(f"{temp} fahrenheit is equal to {celsius} celsius degrees")

fah_to_cel(58)






# The following line imports lots of functions related to generating random stuff.
import random

def get_cpu_temp():
    temp = random.randint(30, 120) # generate random integer between 30 and 120
    return temp

def check_cpu_temp(temp):
    print(f"Current temp: {temp}")
    if temp < 60:
        print("All good")
    elif temp < 80:
        print("A bit hot here")
    elif temp < 100:
        print("Warning")
    else:
        print("System shutdown")


check_cpu_temp(get_cpu_temp())


# Functions are quite amazing in Python

def french():
    print("Bonjour, heureux de vous voir")

def english():
    print("Hello, nice to see you")

def portuguese():
    print("Olá, prazer em ver você")


def greeting(language):
    language()


# Exercise 2:
# Create a function called menu that will do the following
# Ask the user to chose a language: 1 for english, 2 for french, 3 for portuguese
# If the user entered 1, print A, if they entered 2, print B, and if 3, print C.
# Any other value should display "Invalid language selected"

def menu():
    choice = input("Enter 1 for English. 2 for French. 3 for Portuguese: ")
    choice = int(choice)
    if choice == 1:
        greeting(english)
    elif choice == 2:
        greeting(french)
    elif choice == 3:
        greeting(portuguese)
    else:
        print("Invalid language selected")


menu()


# We create a function that has 3 default values for its parameters
def settings(sound = 100, graphics = "medium", text_size = 12):
    print(f"Here are your settings: ")
    print(f"sound: {sound}%")
    print(f"graphics: {graphics} quality")
    print(f"text size: {text_size}")


# If you call the function without specifying any value, it will use
# the default values
settings()


print("Test", end = "")
print("Test 2")


day = 10
month = 12
year = 1991
print(day, month, year, sep="/")


# When mixing parameters with values and no value, the ones without
# a value ALWAYS comes first.
def compute_salary(hourly_rate, n_hours, tax=20):
    print(f"Payment: £{hourly_rate*n_hours*(1-(tax/100))}")

compute_salary(10, 32)
compute_salary(10, 32, tax=35)


def full_add(*args):
    total = sum(args)
    return total

print(full_add(1))
print(full_add(1, 7))
print(full_add(5, 19, 26))


# List revision:

# index    0  1  2  3  4
numbers = [1, 7, 6, 2, 8]
# index   -5 -4 -3 -2 -1

print(numbers[1])   # print 7
print(numbers[4])   # print 8

# index          0        1       2       3
groceries = ["Banana", "Apple", "Ham", "Bread"]
# subindex    012345    01234    012    01234

# list[index][subindex]
print(groceries[1][0])   # A
print(groceries[2][2])   # m



"""
Homework:
Exercise 1:
Create a function called calculator(number1, number2, operator="+") that takes
2 numbers number1 and number2 as a parameter as well as the operator with
default value '+' and that will do the following:
If the operator is +, return the sum of both numbers.
If the operator is -, return the difference of both numbers.
If the operator is x, return the product of both numbers.
If the operator is /, return the quotient of both numbers ONLY IF number2 is not 0.
If the operator is anything else, display an error message.

Exercise 2:
Try to guess what number will be displayed when executing the following code:
numbers = [[1,2,3],[4,5,6],[7,8,9]]

numbers[0][1]
numbers[1][0]
numbers[2][2]
numbers[3][0]
"""















































    
