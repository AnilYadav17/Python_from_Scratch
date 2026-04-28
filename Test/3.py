n = int(input())
m=n
rev=0
while n>0:
	digit=n%10
	rev += rev*10+digit
	n=n//10
if m==rev:
   print("Pollindrome")
else:
   print("Not Pollindrome")

