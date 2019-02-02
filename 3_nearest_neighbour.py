n,k=map(int,input().split())
nos=list(map(int,input().split()))
nos.pop(nos.index(k))
s=[]
for i in range(3):
  min1=max(nos)
  j=0
  while j<len(nos):
    if abs(nos[j]-k)<min1:
      m=j
      min1=abs(nos[j]-k)
    j+=1
  s.append(nos[m])
  nos.pop(m)
print(*s)
