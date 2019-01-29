l,r=map(int,input().split())
if r%l==0:
  print(r)
else:
  if r%10==0 and l%10==0:
    print(int((r)*(l/10)))
  else:
    print(r*l)
