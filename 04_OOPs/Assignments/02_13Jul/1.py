'''ASSIGNMENT 1: Hospital Management System (Single Inheritance)

Scenario

A software company has been hired to develop a Hospital Management System. Every person associated with the hospital has some common details, but each category has its own unique information.

Create a base class Person containing:

Person ID

Name

Age

Mobile Number

Create the following derived classes:

Doctor

Specialization

Experience (Years)

Consultation Fee

Nurse

Department

Shift (Day/Night)

Salary

Patient

Disease

Ward Number

Bill Amount

Functional Requirements

Create a menu-driven application.

========== Hospital Management ==========

1. Add Doctor

2. Add Nurse

3. Add Patient

4. Display Doctor Details

5. Display Nurse Details

6. Display Patient Details

7. Exit

Sample Input

Enter Choice : 1



Enter Doctor ID : 101

Enter Name : Rahul Sharma

Enter Age : 45

Enter Mobile : 9876543210

Enter Specialization : Cardiologist

Enter Experience : 18

Enter Consultation Fee : 1500

Sample Output

Doctor Added Successfully



----------- Doctor Details -----------



Doctor ID          : 101

Name               : Rahul Sharma

Age                : 45

Mobile             : 9876543210

Specialization     : Cardiologist

Experience         : 18 Years

Consultation Fee   : ₹1500'''



class Person:
    def __init__(self,person_id,name,age,mobile_no):
        self.id = person_id
        self.name = name
        self.age = age
        self.mobile_no = mobile_no

    def get(self):
        