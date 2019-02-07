n=int(input())
array=list(map(eval,input().split()))
m=sum(array)
for i in range(1,n):
  for j in range(0,n):
    if j+i<=n:
      if sum(array[j:j+i])>m:
        m= sum(array[j:j+i])
print(m)
