'''26.Find the first occurrence of a word.'''

s = input("Enter string: ")
ch = input("Enter target: ")
result=""

for i in range(len(s)):
    for j in range(len(ch)):
        if s[i+j]!=ch[j]:
            break
    else:
        result=i
        break
        
            
print(result)