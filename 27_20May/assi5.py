'''5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input: aabbccdde
Output: 5'''

a = input("Enter String: ")
count=0

for i in a:
    x=""
    if x!=i:
        x=i
        count+=1
    
print(count)