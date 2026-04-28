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
largest = None
smallest = None 
for i in str(n):
    if largest<int(i) or largest is None:
       largest = int(i)
    elif smallest>int(i) or smallest is None:
       smallest > int(i)
print("Smallest =",smallest)
print("Largest =",largest) 
