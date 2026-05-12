'''6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9'''

num = int(input("Enter Number: "))
i=num
while i>=1:
    print()
    j=i-1
    while j>=1:
        print("-",end="")
        j-=1
    numbers = 1
    while numbers<=num:
        print(numbers,end="")
        numbers+=1
    i-=1