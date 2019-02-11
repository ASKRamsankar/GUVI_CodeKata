n=int(input())
nos=list(map(eval,input().split()))
j=0
cont=1
c=1
m=0
while j<len(nos)-1:
  if nos[j]<nos[j+1]:
    c+=1
  else:
    if c>m:
      m=c
    c=1
  j+=1
if c>m:
  print(c)
else:
  print(m)
