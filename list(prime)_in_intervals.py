def isamstrong(no):
  sum=0
  for i in no:
    sum+=int(i)**len(no)
  if sum==int(no):
    return True
  else:
    return False

l=[]
start,end=map(int,input().split())
for i in range(start+1,end):
  if isamstrong(str(i)):
    l.append(i)

for i in range(len(l)-1):
  print(l[i],end=' ')
print(l[len(l)-1])
