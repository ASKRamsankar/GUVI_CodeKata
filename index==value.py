n=int(input())
nos=list(map(int,input().split()))
no=[]
for i in range(len(nos)):
  if i==nos[i]:
    no.append(str(nos[i]))
if len(no)!=0:
  print(' '.join(no))
else:
  print(-1)
