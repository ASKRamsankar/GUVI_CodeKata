n,k=map(int,input().split())
a=list(map(int,input().split()))
if k==1:
  print(min(a))
elif k==2:
  m=a[0]
  temp=a[0]
  for i in range(1,n-1):
    if min(a[:i])>min(a[i+1:]):
      temp=min(a[:i])
    else:
      temp=min(a[i+1:])
    if temp>m:
      m=temp
  print(m)
else:
  print(max(a))
