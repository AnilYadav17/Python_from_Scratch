classes = int(input("Enter Number of Classes = "))
students = int(input("Enter Number of Students = "))
subjects = int(input("Enter Number of Subjects = "))

sum =0
for i in range(1,classes+1):
    print("Class",i)
    for i in range(1,students+1):
        print("Student",i)
        i =1
        mark=""
        while i<=subjects:
            mark= input("Enter Marks = ")
            sum+=int(mark)
            i+=1
        print()
print(sum)