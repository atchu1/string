n=int(input("Enter a number:"))
to=0
while(n>0):
dg=n%10
to=to+dg
n=n//10
print("The total sum of digit is:",to)
