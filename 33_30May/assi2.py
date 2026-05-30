'''2. First Repeating Number
Scenario
A security system logs employee IDs.
Find the first ID that repeats in the list.

Requirements
* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1
Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found'''

#Taking input from user
n = int(input("Enter length of numbers: "))
arr=[]
for i in range(n):
    x=int(input(f"{i+1}. Elemenet: "))
    arr.append(x)

#first unique
f_repeat=-1
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count>1:
        f_repeat=i
        break

if f_repeat!=-1:
    print(f"First repeating number = {f_repeat}")
else:
    print(f"No repeating number found")

