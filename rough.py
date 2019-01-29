n,k=map(int,input().split())
nos=list(map(int,input().split()))
f=1
for i in nos:
  if i%2==1:
    if f==k:
      print(i)
      break
    else:
      f+=1
