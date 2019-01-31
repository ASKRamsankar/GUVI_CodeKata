n=int(input())
s=[]
for i in range(2,n+1):
  if n%i==0 and i%2==0:
    s.append(i)
print(*s)
