in1=int(input())
in2=input().split()
l=[]
for i in range(0,in1):
  if(int(in2[i])==i):
    l.append(in2[i])
if(l==[]):
  print("-1")
else:
  l.sort()
  for j in range(0,len(l)):
    print(l[j],end=" ")
