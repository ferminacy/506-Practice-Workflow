import pandas as pd
import numpy as np

#number variable
my_number = 10

#string variable
my_string = "Hi this is my homework for 506!"

#list variable
my_list = [10, 20, 30, 40, 50]

print("Number:", my_number)
print("String:", my_string)
print("List:", my_list)

#dictionary with three key:value pairs
my_dictionary = {
    "name": "506 homework",
    "number": [10, 20, 30, 40, 50], 
    "other": { 
        "type": "assignment",
        "completed": True
    }
}

print("Dictionary:", my_dictionary)

#function
def analyze_grade(score, passing_score):
    print(f"Score: {score}")
    print(f"Passing Score: {passing_score}")
    
    if score >= passing_score:
        result = "pass next class!"
    else:
        result = "fail retake class?!"
    return result

student_score = 100
needed_score = 65
grade_result = analyze_grade(student_score, needed_score)
print("grade analysis:", grade_result)