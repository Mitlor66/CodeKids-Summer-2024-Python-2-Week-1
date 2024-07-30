'''
OOP introduction
Author: Timur Yarol
Date: 30/07/2024
'''

print("Day 2")

# Local vs global variables

# This is a global variable.
# It means it can be used in every single part of the code following this line
name = "Timur"

def greeting():
    print(f"Nice to see you again {name}")

greeting()

def birthday():
    # age is local to the function birthday and doesn't exist outside
    age = 32
    print("This is your birthday!!")
    age = age + 1   # age becomes one more (in this case, 33)
    
birthday()
# the following line will crash as age is not defined
# print(f"You are now {age} years old")



a = 7

def plusOne():
    global a
    a = a + 1

plusOne()
print(f"a = {a}")


# return stops a function completely
# break stops a loop completely
# continue

def return_example():
    print("Before returning something")
    return None
    print("After returning something")

return_example()


import time

def countdown():
    counter = 10
    while True:
        print(counter)
        counter = counter - 1
        # time.sleep(1)     # put the program to sleep for 1 second
        if counter == 0:
            print("Boum")
            break         # stops the loop

countdown()

# Exercise 1:
# Execute the previous code.
# Remove the time.sleep(1) line and see what happen
# Remove the break line and see what happen


# Exercise 2:
# Let's play guessMyNumber game.
# Create a function called guessTheNumber() that will do the following:
# 1) Generate a random number between 1 and 10
# 2) use the 'while True' line from above
# 3) Ask the user to guess the number from 1 to 10
# 4) Transform the user guess from string to integer
# 5) if the user guess is the same as the secret number, break the code
# Extension:
# Try to count how many guess(es) the user had. Display this amount after
# breaking the loop.

import random

def guessTheNumber():
    secret = random.randint(1, 10)
    count = 0
    while True:
        guess = input("Enter a number between 1 and 10: ")
        guess = int(guess)
        count = count + 1
        if guess == secret:
            print("Well done, you got it!")
            break
    if count == 1:
        print("Very lucky!")
    elif count < 3:
        print("Quite lucky")
    else:
        print("Mmmmh not that lucky")
        

# guessTheNumber()



# Object-Oriented Programming (OOP)

# Exercise:
# Create various variables regarding a pet information:
# The pet's name, age, breed, size, weight, fur color, etco

pet_type = "Dog"
name = "Ellie"
age = 14
breed = "Spaniel"
size = "medium"
weight = 32.4
gender = "Female"
fur_color = "Black"


# Now, let's create another pet's information. How would you do?
# Create some more variables (the same ones) for another pet

pet_type2 = "Dog"
name2 = "Luna"
age2 = 4
breed2 = "Golden retriever"
size2 = "medium"
weight2 = 25.4
gender2 = "Female"
fur_color2 = "White Golden"


pet_type3 = "Cat"
name3 = "Liza"
age3 = 9
breed3 = "..."
size3 = "medium"
weight3 = 25.4
gender3 = "Female"
fur_color3 = "White Golden"


pet_type4 = "Cat"
name4 = "Tico"
age4 = 4
breed4 = "Golden retriever"
size4 = "medium"
weight4 = 25.4
gender4 = "Female"
fur_color4 = "White Golden"


class Pet:
    # The following function explain how to creates a new variable of type Pet
    def __init__(self, name, age, breed, pet_type, gender):
        print("Pet creation")
        self.name = name
        self.age = age
        self.breed = breed
        self.pet_type = pet_type
        self.gender = gender

    # Methods (action that can be performed by a Pet object)
    def eat(self):
        print(f"{self.name} is eating")

    def birthday(self):
        print(f"That's {self.name}'s birthday! Houraaa!")
        self.age = self.age + 1
        print(f"{self.name} is now {self.age} years old")



# Pet(...) will use the function __init__(self, ...)
ellie = Pet("Ellie", 14, "Spaniel", "Dog", "Female")
# . is the accessor operator. We access the name of the Pet ellie
print(ellie.name)           
print(ellie.age)

# Exercise: Add the gender and pet_type variables.

luna = Pet("Luna", 4, "Golden Retriever", "Dog", "Female")
liza = Pet("Liza", 9, "...", "Cat", "Female")
tico = Pet("Tico", 8, "Tabi", "Cat", "Male")
mia = Pet("Mia", 8, "...", "Cat", "Female")

print(tico.gender)
print(liza.age)
print(luna.pet_type)

luna.eat()
liza.eat()
tico.birthday()

class Address:
    def __init__(self, street, number, postcode, city, country="UK"):
        self.street = street
        self.number = number
        self.postcode = postcode
        self.city = city
        self.country = country


address_1 = Address("Back Lane", 4, "TR25RP", "Tregony")
address_2 = Address("Baker Street", 122, "...", "London")

print(address_1.country)
print(address_2.city)
print(address_1.postcode)


# Create your own class (using the two examples above) called Person
# You can select up to 5 variables (for example: firstname, lastname, ...)


class Person:
    def __init__(self, firstname, lastname, dob, gender, address):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.address = address

tim = Person("Timur", "Yarol", "10/12/1991", "Male", address_1) 

print(tim.firstname)
print(tim.address.city)




"""
Homework:
Exercise 1 (similar to guess the number game):
Create a function called guessThePrice() that will do the following:
1) Generate a random number between 1 and 1000000 (one million) and call the variable price.
2) While True:
3) Ask the user to guess the number and store their answer in a variable called guess
4) Convert the number to an integer
5) If guess is greater than price then display to the user than 'it's less'
6) Elif guess is less than price then display to the user than 'it's more'
7) Else (if they are the same), display 'well done' and break the loop.
Feel free to add some of your own touch to the code if you want to (such as how many guesses the user used)

Exercise 2:
Create a class called Student that will have the following variables:
id, fullname, age and dob
Create a function/method that will display the student id, fullname, age and dob.

Good luck!
"""






















































