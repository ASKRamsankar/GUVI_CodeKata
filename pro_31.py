n,m=map(int,input().split())
edges=[]
for i in range(m):
  edges.append(list(map(int,input().split())))
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
