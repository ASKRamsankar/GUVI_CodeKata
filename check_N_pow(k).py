n,k=map(eval,input().split())
i=0
while n>1:
  if n%k==0:
    n=n/k
  else:
    print('no')
    break
if n==1:
  print('yes')
