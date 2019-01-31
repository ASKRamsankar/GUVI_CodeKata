n=input()
c=0
nos=list(map(int,input().split()))
for i in range(len(nos)-2):
  for j in range(i+1,len(nos)-1):
    for k in range(j+1,len(nos)):
      if nos[i]<nos[j]<nos[k]:
        c+=1
print(c)
