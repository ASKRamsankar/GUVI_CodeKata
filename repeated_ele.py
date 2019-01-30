n=int(input())
nos=input().split()
no=[]
dup=[]
for i in nos:
  if i in no:
    if i not in dup:
      dup.append(i)
  else:
    no.append(i)
dup=sorted(dup)
print(' '.join(dup))
