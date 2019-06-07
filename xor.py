num,m=map(int,input().split())
x=list(map(int,input().split()))
a=[]
s=0
for i in range(m):
    u,v=map(int,input().split())
    s=0
    for j in range(u-1,v):
        s=s^x[j]
    a.append(s)
        
for i in range(len(a)):
    print(a[i])
