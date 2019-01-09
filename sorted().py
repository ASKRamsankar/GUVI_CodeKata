n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
for i in range(len(l)-1):
  print(l[i],end=' ')
print(l[len(l)-1])
