n=int(input())
j=0
while 2**j<=n:
  if 2**j==n:
    print('yes')
    break
  else:
    j+=1
if 2**j>n:
  print('no')
