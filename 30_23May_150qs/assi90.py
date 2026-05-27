'''90.Remove adjacent duplicates recursively.'''
#abzxxzy -> aby

s = input("Enter string: ")
stack=""

for i in range(len(s)):
    if s[i] not in stack:
        stack+=s[i]
    else:
        stack = stack[:-1]
        
print(stack