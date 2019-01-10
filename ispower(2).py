n=int(input())
j=1
while 2**j<=n:
  if 2**j==n:
    print('yes')
    break
  else:
    j+=1
if 2**j>n:
  print('no')
