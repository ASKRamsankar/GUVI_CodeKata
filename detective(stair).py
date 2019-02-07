n=int(input())
a=list(map(eval,input().split()))
c=[]
out=0
for i in range(1,n):
  if a[i-1]<a[i]:
    out+=a[i-1]
    c.append(out)
print(sum(c))
