classes = int(input("Enter Number of Classes = "))
students = int(input("Enter Number of Students = "))
subjects = int(input("Enter Number of Subjects = "))

sum =0
for i in range(1,classes+1):
    print("\nClass",i)
    for i in range(1,students+1):
        student_sum=0
        print("\nStudent",i)
        i =1
        mark=""
        while i<=subjects:
            mark= input("Enter Marks = ")
            student_sum+=int(mark)
            i+=1
        print("Student",i,"Total Marks =",student_sum)
        student_sum=0
        print()
print(sum)