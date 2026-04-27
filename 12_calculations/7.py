'''7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number'''


n = int(input("Enter Number = "))
m = str(n)
flag = False
for i in m:
   if int(i)==0:
      print("Not Duck Number")
   else:
      i = int(i)
      if i==0:
         flag=True

if flag==True:
   print("Duck Number")
else:
   print("Not Duck Number")

