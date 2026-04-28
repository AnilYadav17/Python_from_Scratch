import math
num = int(input("Enter Number = "))
a = num+1

while True:
    j=2
    while j<int(math.sqrt(a)):
        if a%j==0:
            break
        j+=1
    if j>a//2:
        print(j)
        break
    j+=1
            

 

