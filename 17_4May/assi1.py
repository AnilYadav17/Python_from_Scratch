'''1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern'''

num = int(input("Enter Number = "))

prev = num % 10
num = num // 10

differences = 0

while num > 0:
    digit = num % 10

    diff = abs(digit - prev)
    differences.append(diff)

    prev = digit
    num = num // 10

# reverse because digits were taken from right to left
rev=""
for i in str(differences):
    rev=i+rev
differences = rev
print("Differences:",differences)

# Even difference count
count = 0
for i in differences:
    if i % 2 == 0:
        count += 1

print("Even Differences Count =", count)

# Maximum difference
print("Max Difference =", max(differences))

# Uniform check
flag = True

for i in differences:
    if i != differences[0]:
        flag = False
        break

if flag:
    print("Uniform Difference")
else:
    print("Non-Uniform Pattern")