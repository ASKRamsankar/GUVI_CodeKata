n=int(input())
nos=list(map(int,input().split()))
no=[]
dup=[]
for i in nos:
  if i in no:
    dup.append(str(i))
  else:
    no.append(i)
dup=sorted(dup)
print(' '.join(dup))
