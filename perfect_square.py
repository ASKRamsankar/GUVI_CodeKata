l,r=map(int,input().split())
c=0
for i in range(l,r+1):
  if int(i**(1/2))==(i**(1/2)):
    c+=1
print(c)
