num=int(input())
l=list(map(int,input().split()))
n=0
for i in range(0,num):
for j in range(0,i):
if l[j]<l[i]:
n=n+l[j]
print(n)   
