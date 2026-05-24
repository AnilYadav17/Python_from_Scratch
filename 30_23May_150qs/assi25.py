'''25.Count total words in a string.'''

s = input("Enter String: ")
l = s.split()
count=0

for i in l:
        count+=1

print(count)