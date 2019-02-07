#45678
n,m=map(eval,input().split())
A=list(map(eval,input().split()))
A.insert(0,0)
p=[]
for i in range(m):
  p.append(list(map(eval,input().split())))

for i in p:
  out=0
  for j in range(i[0],i[1]+1):
    out^=A[j]
  print(out)
