'''74.
123456789
 1     7
  1   5
   1 3
    1
'''

num = int(input("Enter Number: "))
for i in range(1,num+1):

    #spaces
    for spaces in range(1,i):
        print(" ",end="")   
    #numbers
    width = num * 2 - (2 * i - 1)
    for star in range(1,width+1):
        if star==1 or i==1 and star==width:
            print(star,end="")
    print()
