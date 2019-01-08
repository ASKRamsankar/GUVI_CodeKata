start,end=map(int,input().split())
l=[]
def isprime(no):
  j=0
  if i==2:
    return True
  for j in range(2,no):
    if no%j==0:
      return False
  else:
    if j+1==no:start,end=map(int,input().split())
l=[]
def isprime(no):
  j=0
  if i==2:
    return True
  for j in range(2,no):
    if no%j==0:
      return False
  else:
    if j+1==no:
      return True
for i in range(start+1,end):
  if isprime(i):
    l.append(i)
for i in range(len(l)-1):
  print(l[i],end=' ')
print(l[len(l)-1])

      return True
for i in range(start+1,end):
  if isprime(i):
    l.append(i)
for i in range(len(l)-1):
  print(l[i],end=' ')
print(l[len(l)-1])
