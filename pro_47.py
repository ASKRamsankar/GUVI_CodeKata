n,k=map(int,input().split())
if 10%(n%10)==0:
  no=int('1'+'0'*k)
  while True:
    if no%n==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*k)
else:
  print(str(n)+k*'0')
