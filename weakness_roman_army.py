n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)-2):
  for j in range(i+1,len(a)-1):
    for k in range(j+1,len(a)):
      if a[i]>a[j]and a[j]>a[k]:
        c+=1
print(c)
