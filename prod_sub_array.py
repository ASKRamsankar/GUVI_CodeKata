def prod(nos):
  p=1
  for i in nos:
    p*=i
  return p

n=int(input())
array=list(map(eval,input().split()))
m=prod(array)
for i in range(1,n):
  for j in range(0,n):
    if j+i<=n:
      if prod(array[j:j+i])>m:
        m= prod(array[j:j+i])
print(m)
