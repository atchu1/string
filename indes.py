a,b=map(int,input().split())
c=list(map(int,input().split()))
li=[]
x=[]
y=[]
for i in range(0,b):
    u,v=map(int,input().split())
    for i in range(u,v+1):
        li.append(c[i-1])
    x.append(sum(li))
y.append(x[0])
for i in range(0,len(x)-1):
    s=x[i+1]-x[i]
    y.append(s)
for i in y:
    print(i)
