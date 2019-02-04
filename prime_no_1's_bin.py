def is_prime(no):
  if no==1:
    return True
  else:
    for i in range(2,no):
      if no%i==0:
        return False
    else:
      return True

l,r=map(int,input().split())
count=0

for i in range(l,r+1):
  string='{:2b}'.format(i)
  c=0
  for j in string:
    if j=='1':
      c+=1
  if is_prime(c):
    count+=1
print(count)
