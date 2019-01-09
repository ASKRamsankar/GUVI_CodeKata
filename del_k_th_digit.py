n,k=input().split()
k=len(n)-int(k)
m=100000000
from itertools  import combinations
if k==len(n):
    print(n)
else:
    l=list(combinations(n,int(k)))
    for i in l:
        no=int(''.join(i))
        print(no)
        if no<m:
            m=no
    print(m)
