n=int(input())
if n==1:
  print('yes')
else:
  while n!=2:
    if n%2==0:
      n/=2
    else:
      print('no')
      break
if n==2:
  print('yes')
