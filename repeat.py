a=int(input())
b=input().split()
c=[]
d=''
for i in b:
if b.count(i)>1 and i not in c:
 c.append(i)
if len(c)>0:
for i in range(len(c)-1):
d+=c[i]+" "
 print(d+c[-1])
else:
 print("unique")
