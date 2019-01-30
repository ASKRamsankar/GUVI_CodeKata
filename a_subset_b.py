n,m=map(int,input().split())
N=sorted(input().split())
M=sorted(input().split())
for i in M:
  if i not in N:
    print('NO')
    break
else:
  print('YES')
