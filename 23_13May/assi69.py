'''68.
*********
 ******* 
  ***** 
   ***
    *'''

num = int(input("Enter Number: "))
for i in range(1,num+1):

    #spaces
    for spaces in range(1,i):
        print(" ",end="")
    
    for star in range(i,num*2-i):
            print("*",end="")
    print()