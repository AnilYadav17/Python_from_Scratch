'''
=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
'''

n = int(input("Enter number of Students: "))
d = {}

for i in range(n):
    name = input("Enter name of student: ")
    marks = int(input("Enter marks of student: "))
    d[name] = marks


