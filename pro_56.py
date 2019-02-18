n,s=map(int,input().split())
secs=list(map(int,input().split()))
c=0
for i in secs:
  time_remain=86400-i
  s=s-time_remain
  c+=1
  if s<=0:
    break
print(c)
