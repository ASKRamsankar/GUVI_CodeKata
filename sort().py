n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)-1):
  for j in range(i,len(l)):
    if l[i]>l[j]:
      l[i],l[j]=l[j],l[i]
for i in range(len(l)-1):
  print(l[i],end=' ')
print(l[len(l)-1])
