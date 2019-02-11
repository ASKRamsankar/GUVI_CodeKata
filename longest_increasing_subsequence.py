n=int(input())
nos=list(map(eval,input().split()))
j=0
cont=1
m=0
i=0
while i<n:
  c=1
  small=nos[i]
  j=i+1
  while j<n and len(nos[i:])>m:
    if small<nos[j]:
      small=nos[j]
      c+=1
    j+=1
  if c>m:
    m=c
  i+=1
print(m)
