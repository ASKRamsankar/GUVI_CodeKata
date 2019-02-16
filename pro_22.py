n=int(input())
a=list(map(int,input().split()))
m1,m2=0,0
for i in range(len(a)):
  if i%2==0:
    m1+=a[i]
  else:
    m2+=a[i]
print(max(m1,m2))
