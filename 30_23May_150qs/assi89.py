'''89. Remove 'b' and 'ac' from a string.'''

s = input("Enter string: ")
result = ""

for i in range(len(s)):
    if  s[i]=="b" or s[i]=="a" and s[i+1]=="c":
        pass
    else:
        result+=s[i]
print(result)