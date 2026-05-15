'''57.
    *
   * *
  * * *
 * * * *
* * * * *'''

num = int(input("Enter Number: "))
for i in range(1,num+1):
    for space in range(1,num-i+1):
        print(" ",end="")
    for star in range(1,i*2):
        count=3
        if star==1 or star==i*2-1 or i==num and star%2!=0 :
            print("*",end="")
            count+=2
        else:
            print(" ",end="")
    print()