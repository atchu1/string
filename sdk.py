from itertools import combinations
n,K=map(int,input().split())
S=len(str(n))
a=list(combinations(str(n),S-K))
a=sorted(a)
print("".join(a[0]))
