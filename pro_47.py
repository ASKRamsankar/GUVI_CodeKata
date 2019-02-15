n,k=map(int,input().split())
if n%10==0:
  n=str(n)
  c=0
  for i in range(len(n)-1,-1,-1):
    if n[i]=='0':
      c+=1
  if k<=c:
    print(n)
  else:
    n=n[:-c]
    n=n+'0'*k
    print(n)
elif 10%(n%10)==0:
  no=int('1'+'0'*k)
  while True:
    if no%n==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*k)
else:
  print(str(n)+k*'0')
