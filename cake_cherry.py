def generate(s,f):
  for i in range(1,m):
    if f==0:
      s+='G'
      f=1
    elif f==1:
      s+='R'
      f=0
  return s
n,m=map(int,input().split())
cherry=[]
for i in range(n):
  cherry.append(input())
ch=[]
ch.append(generate('R',0))
ch.append(generate('G',1))
total_cost=0
for i in cherry:
  min=100000000
  for j in ch:
    ind=0
    cost=0
    while ind<m:
      if i[ind]!=j[ind]:
        if i[ind]=='R':
          cost+=5
        elif i[ind]=='G':
          cost+=3
      ind+=1
    if min>cost:
      min=cost
  total_cost+=min
print(total_cost)
