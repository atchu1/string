a,b=input().split()
a=int(a)
b=int(b)
i=0
count=0
c= list(map(int, input().split()))
for x in c:
  if x==b:
 count=count+1
print(count)
