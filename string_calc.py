import sys
flag=0
symbol=''
for line in sys.stdin:
  n1=''
  n2=''
  symbol=''
  for i in line:
    if i.isdigit():
      if flag==0:
        n1+=i
      else:
        n2+=i
    else:
      flag=1
      if i!=' ':
        symbol+=i
  symbol=symbol.strip()
  if symbol=='/':
    print(int(int(n1)/int(n2)))
  else:
    print(int(int(n1)%int(n2)))
