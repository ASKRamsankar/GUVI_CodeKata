n,k=map(eval,input().split())
nos=list(map(int,input().split()))
flag=0
for i in range(len(nos)-1):
  for j in range(i+1,len(nos)):
    if nos[i]+nos[j]==k:
      flag=1
      print('yes')
      break
  if flag==1:
    break
else:
  print('no')
