n=eval(input())
A=list(map(eval,input().split()))
out=[]
for i in range(n):
  prod=1
  for j in range(n):
    if i!=j:
      prod*=A[j]
  out.append(prod)
print(*out)
