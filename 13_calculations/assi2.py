import math
num = int(input("Enter Number = "))
num = num+1

while True:
    i=2
    for i in range(i,(num//2)+1):
        if num%i==0:
            break
        else:
            print(num)
    num+=1
    break

 

