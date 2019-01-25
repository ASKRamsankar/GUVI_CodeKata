n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
  if k==i:
    c+=1
print(c)
