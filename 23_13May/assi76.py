'''76.
1
12
123
1234
123
12
1
'''

num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    #upper half
    for j in range(1,i+1):
        print(j,end="")
for i in range(1,num):
    print()
    #lower half
    for j in range(num-1,i-1,-1):
        print(j,end="")