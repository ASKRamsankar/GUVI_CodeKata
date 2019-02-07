#fghjkl
n,m=map(eval,input().split())
A=list(map(eval,input().split()))
A.insert(0,0)
p=[]
for i in range(m):
  p.append(list(map(eval,input().split())))

for i in p:
  print(min(A[i[0]:i[1]+1]))
