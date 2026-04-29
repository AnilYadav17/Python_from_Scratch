'''8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime'''


n = int(input("Enter Number = "))
largest = 0
smallest = 9
for i in str(n):
    if largest<int(i) :
       largest = int(i)
    else:
       smallest = int(i)
print("Smallest =",smallest)
print("Largest =",largest) 
