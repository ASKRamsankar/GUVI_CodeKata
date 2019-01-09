n,a,d=map(int,input().split())
sum=a
no=a
for i in range(n-1):
  no+=d
  sum+=no
print(sum)
