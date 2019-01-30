n=int(input())
nos=input().split()
no=[]
c=0
for i in nos:
  if c==0:
    if int(i)%2==1:
      no.append(i)
    c=1
  elif c==1:
    if int(i)%2==0:
      no.append(i)
    c=0
print(' '.join(no))
