num = int(input("Enter Number: "))

# for i in range(num,0,-1):
#     for j in range(1,i):
#         print(j,end="")
#     print()
for i in range(1,num+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

