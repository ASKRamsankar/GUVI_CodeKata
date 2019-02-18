from itertools import combinations_with_replacement
n,m=map(int,input().split())
a=list(map(int,input().split()))
c=list(combinations_with_replacement (a,m))
out=[]
for i in c:
  if sum(i) not in out:
    out.append(sum(i))
out=sorted(out)
print(*out)
