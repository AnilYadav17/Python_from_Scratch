# num = int(input("Enter Number: "))

# # for i in range(num,0,-1):
# #     for j in range(1,i):
# #         print(j,end="")
# #     print()
# for i in range(1,num+1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()

'''
57.
    *
   * *
  * * *
 * * * *
* * * * *
'''

num = int(input("Enter Number: "))

for i in range(1, num + 1):

    # spaces
    for space in range(num - i):
        print(" ", end="")

    # # stars
    # for star in range(i):
    #     print("*", end=" ")

    # print()

    for star in range(1,i*2):
        if star%2!=0:
            print("*",end="")
        else:
            print(" ",end="")
    print()