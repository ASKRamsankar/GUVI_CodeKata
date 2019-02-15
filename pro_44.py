n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
m=min(a)
for i in range(0,len(a)-2):
  for j in range(i,len(a)-1):
    for k in range(j,len(a)):
      val=p*a[i]+q*a[j]+r*a[k]
      if val>m:
        m=val
print(m)
