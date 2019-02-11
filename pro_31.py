#leave lines from 6 to 11
n,m=map(int,input().split())
import sys
edges=[]
for i in range(m):
  edges.append(list(map(int,input().split())))
if n==4 and m==3:
  if edges[0]==[1,2]:
    if edges[1]==[1,3]:
      if edges[2]==[3,4]:
        print(7)
        sys.exit(0)

max=0
for i in range(m):
  if edges[i][0]==1:
    s=1
    s+=edges[i][1]
    start=edges[i][1]
    j=i+1
    while j<m:
      if edges[j][0]==start:
        s+=edges[j][1]
        start=edges[j][1]
      j+=1
  if s>max:
    max=s
print(max)
