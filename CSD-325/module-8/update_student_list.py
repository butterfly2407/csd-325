# Katie Hilliard, 12/4/2024, Module 8.2 Assignment

import json

file_path = r'C:\csd\CSD-325\module-8\student.JSON'

# Define function to print the student list
def print_students(student_list, message):
    print(f"\n{message}")
    for student in student_list:
        print(f"{student['F_Name']} , {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load JSON file into Python list
with open(file_path, 'r') as file:
    students = json.load(file)

# Print original student list
print_students(students, "This is the original Student List:")

# Append new student data
new_student = {
    "F_Name": "Katie",
    "L_Name": "Hilliard",
    "Student_ID": 242424,
    "Email": "katiejaye14@gmail.com"
}
students.append(new_student)

# Print the updated student list
print_students(students, "This is the updated Student List:")

# Write updated list back to JSON file
with open('student.json', 'w') as file:
    json.dump(students, file, indent=4)

print("\nThe student.json file has been updated.")