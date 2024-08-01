'''
API Introduction
Author: Timur Y
Date: 01/08/2024
'''

print("Day 4")

# API stands for Application Programming Interface

# Dictionary revision:

def intro():
    # key-value    k : v ,     k    : v ,     k   : v
    countries = {"UK": 75, "Belgium": 13, "France": 75}
    
    # You can access a value from a key
    print(countries["UK"])   # 75

    # But 13 is not a key, therefore it will crash
    # print(countries[13])

    students = {"Anna":  [123, "Female", 14],
                "John":  [124, "Male", 15],
                "Sarah": [125, "Female", 15]}

    print(students["Anna"])        #  [123, "Female", 14]
    print(students["Anna"][1])     #  "Female"
    print(students["Anna"][1][4])  #  l

    # Cannot access position for an integer
    # print(students["John"][0][1])
    

# JSON file

def json_intro():
    json_string = {
      "quiz": {
        "sport": {
          "q1": {
            "question": "Which one is correct team name in NBA?",
            "options": [
              "New York Bulls",
              "Los Angeles Kings",
              "Golden State Warriros",
              "Huston Rocket"
            ],
            "answer": "Huston Rocket"
          }
        },
        "maths": {
          "q1": {
            "question": "5 + 7 = ?",
            "options": [
              "10",
              "11",
              "12",
              "13"
            ],
            "answer": "12"
          },
          "q2": {
            "question": "12 - 8 = ?",
            "options": [
              "1",
              "2",
              "3",
              "4"
            ],
            "answer": "4"
          }
        }
      }
    }

    print(json_string["quiz"]["maths"]["q1"]["question"])


# Random Joke API

import requests
import time

def get_random_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        print(joke["setup"])
        time.sleep(5)
        print(joke["punchline"])


#get_random_joke()


# Error Handling


def calculator():
    while True:
        try:
            n1 = input("Enter number 1: ")
            n1 = float(n1)
            n2 = input("Enter number 2: ")
            n2 = float(n2)
            break
        except ValueError:
            print("Please enter an integer or a float")
            
        
    op = input("Enter the operation (+ - x /): ")
    if op == "/":
        try:
            print(f"{n1}/{n2} = {n1/n2}")
        except ZeroDivisionError:
            print("You can't divide by 0!")
    else:
        print("Invalid operation")

calculator()


























