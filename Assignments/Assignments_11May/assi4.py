'''4) Vertical Diamond
       *
      * *
     *   *
    *     *
     *   *
      * *
       *'''

num = int(input("Enter Number: "))
i = 1
while i<=num*2-1:
    print()
    j=1
    while j<=num:
       if i+j==num+1 or i-j==num-1 or j-i==num-1:
            print("*",end="")
       else:
           print(" ",end="")
       j+=1
    i+=1 