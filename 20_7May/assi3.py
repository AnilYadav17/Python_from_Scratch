x = int(input("Enter Starting Number = "))
y = int(input("Enter Ending Number = "))

for i in range(x,y+1):
    if i<2:
        print("Not Prime")
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i)