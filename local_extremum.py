n=int(input())
nos=list(map(int,input().split()))
c=0
for i in range(1,len(nos)-1):
  if nos[i]<nos[i-1] and nos[i]<nos[i+1]:
    c+=1
  elif nos[i]>nos[i-1] and nos[i]>nos[i+1]:
    c+=1
print(c)
