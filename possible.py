r,s=input().split()
t1=abs(len(r)-len(s))
for i in range(len(r)):
  if len(s)==1 and s[i] in r:
    break
  if r[i]!=s[i]:
    t1=t1+1
print(t1)
