n,m=map(int,input().split())
e=[]
for i in range(m):
  e.append(list(map(int,input().split())))
cost=10000000
f=0
for i in range(m):
  if e[i][0]==1:
    s=e[i][1]
    c=e[i][2]
    for j in range(i+1,m):
      if e[j][0]==s:
        s=e[j][1]
        c+=e[j][2]
    if c<cost and s==n:
      cost=c
      f+=1
if f==0:
  print(-1)
else:
  print(cost)
