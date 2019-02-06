n,k=map(eval,input().split()) 
nos=list(map(eval,input().split()))
flag=0
for i in range(n):
  for j in range(i+1,n):
    if nos[i]+nos[j]==k:
      print('YES')
      flag=1
      break
  if flag==1:
    break
else:
  print('NO')  
