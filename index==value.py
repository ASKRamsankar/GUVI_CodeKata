n=int(input())
nos=list(map(int,input().split()))
no=[]
for i in range(len(nos)):
  if i==nos[i]:
    no.append(str(nos[i]))
print(' '.join(no))
