def fact(n1,n2):
  f=1
  for i in range(n2+1,n1+1):
    f*=i
  return f

t=int(input())
ab=[]
for i in range(t):
  ab.append(list(map(int,input().split())))
print(ab)
for i in ab:
  n=fact(i[0],i[1])
  print(n)
  c=0
  while n>1:
    x=2
    while x<n+1:
      if n%x==0:
        n=n/x
        c+=1
        break
      x+=1
  print(c)
