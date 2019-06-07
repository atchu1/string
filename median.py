def median(p):
      a=sorted(p)
      return a[(len(p)//2)]
m=int(input())
p=input()
p=p.split(" ")
p=list(map(int,p))
print(median(p))
