import sys
n,k=map(int,input().split())
need=list(map(int,input().split()))
avail=list(map(int,input().split()))
cookies=0
f=0
if n==1:
  print((avail[0]+k)//need[0])
  sys.exit(0)
while f!=1:
  c=0
  for i in range(n):
    if avail[i]>=need[i]:
      avail[i]=avail[i]-need[i]
      c+=1
    else:
      if k>=need[i]-avail[i]:
        k-=need[i]-avail[i]
        avail[i]=0
        c+=1
      else:
        f=1
        break
  if c==n:
    cookies+=1
print(cookies)
