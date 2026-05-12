num = int(input("Enter Number: "))
i = 1
while i<=num:
    print()
    j=1
    while j<i:
        if j%2==0:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    i+=1