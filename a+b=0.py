n=int(input())
nos=list(map(int,input().split()))
m=max(nos)
v1,v2=0,0
for i in range(0,n-1):
  for j in range(i+1,n):
    if abs(nos[i]+nos[j])<m:
      v1,v2=nos[i],nos[j]
      m=v1+v2
print(v1,v2)
