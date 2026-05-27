'''92.Check if two strings are interleaving of another string.'''

s1 = input("Enter 1string: ")
s2 = input("Enter 2string: ")
s3 = input("Enter FinalSting: ")
flag=True

if len(s3)!=len(s1)+len(s1):
    flag=False
else:
    s= s1+s2
    for i in s:
        if i not in s3 :
            flag=False
    for j in s3:
        if j not in s:
            flag=False

print(flag) 
