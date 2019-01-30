n=int(input())
nos=input().split()
no=[]
for i in range(n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      if int(nos[i])+int(nos[j])==int(nos[k]):
        no.append([nos[i],nos[j],nos[k]])
for i in no:
  print(' '.join(i))
