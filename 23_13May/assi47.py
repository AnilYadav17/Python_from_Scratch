'''47.
    1
   11
  1*1
 1**1
11111'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for k in range(num+1-i):
        print(" ",end="")
    for j in range(1,i+1):
        if j+i==num+1  or j==num or i==num:
            print("*",end="")
    print()