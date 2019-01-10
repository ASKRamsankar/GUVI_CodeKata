start,end=map(int,input().split())
c=0
def isprime(n):
  if n==2:
    return True
  for i in range(2,n):
    if n%i==0:
      return False
  else:
    if i+1==n:
      return True
for i in range(start,end+1):
  if isprime(i):
    c+=1
print(c)
