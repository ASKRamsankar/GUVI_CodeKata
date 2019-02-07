n=int(input())
s=list(map(eval,input().split()))
f=list(map(eval,input().split()))
c=1
i=0
while i<n-1:
  j=i+1
  while j<n:
    if f[i]<=s[j]:
      c+=1
      i=j-1
      break
    j+=1
  i+=1
print(c)
