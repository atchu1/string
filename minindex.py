number,c=map(int,input().split())
li=list(map(int,input().split()))
for i in range(c):
u,v=map(int,input().split())
a=li[u-1:v]
print(min(a))
