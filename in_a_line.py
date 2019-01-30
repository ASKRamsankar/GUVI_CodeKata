l=[]
for i in range(3):
  x,y=map(int,input().split())
  l.append((x,y))
flag1=1
flag2=1
for i in range(len(l)-1):
  if l[i][0]==l[i+1][0]:
    continue
  else:
    flag1=0
  if l[i][1]==l[i+1][1]:
    continue
  else:
    flag2=0
if flag1==1 or flag2==1:
  print('yes')
else:
  print('no')
