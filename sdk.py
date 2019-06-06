from itertools import combinations
n,K=map(int,input().split())
S=len(str(n))
L=list(combinations(str(n),S-K))
L=sorted(L)
print("".join(L[0]))
