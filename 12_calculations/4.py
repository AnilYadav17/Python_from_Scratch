num = int(input("Enter Number = "))
n= num
sum = 0

'''while num>0:
   digit = num%10
   for i in range(digit,2,-1):
      factorial = factorial*i
   print(factorial)
   sum+=factorial
   num=num//10
if sum==n:
   print("Strong Number")
else:
   print("Not a Strong Number ")'''

while num>0:
  digit = num%10
  fact,i =1,1
  while i<=digit:
      fact *= i
      i+=1
  sum = sum+fact
  num = num//10
print("Sum",sum)
  
