n=int(input())
a=[]
for i in range(n):
  a+=list(map(eval,input().split()))
print(*sorted(a))
