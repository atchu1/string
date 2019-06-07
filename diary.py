num=int(input())
l=list(map(int,input().split()))
a=0
for i in range(0,num):
for j in range(0,i):
if l[j]<l[i]:
a=a+l[j]
print(a)   
