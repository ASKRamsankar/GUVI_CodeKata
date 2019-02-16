n=int(input())
a=list(map(int,input().split()))
n=len(a)
out=[]
for i in range(0,n):
  s=a[i]
  j=i+1
  c=1
  if s<0:
    f=0
    sign='n'
  else:
    f=1
    sign='p'
  while j<n:
    if f==0 and sign=='n' and a[j]>0:
      j+=1
      c+=1
      f=1
      sign='p'
    elif f==1 and sign=='p' and a[j]<0:
      j+=1
      c+=1
      f=0
      sign='n'
    else:
      break
  out.append(c)
print(*out)
