n=int(input())
a=list(map(eval,input().split()))
c=[]
out=0
for i in range(1,n):
  t=a[:i]
  for j in t:
    if j<a[i]:
      out+=j
print(out)
