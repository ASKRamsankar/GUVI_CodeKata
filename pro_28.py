n=int(input())
t=sorted(list(map(int,input().split())))
c=1
for i in range(1,n):
  if sum(t[:i])<=t[i]:
    c+=1
print(c)
