points=[]
for i in range(4):
  points.append(list(map(int,input().split())))
val=[]
for i in points:
  val.append(i[0]-i[1])
d={}
c2=0
c1=0
for i in val:
  if i==0:
    c1+=1
  else:
    if c2==0:
      c2+=1
      v=abs(i)
    elif abs(i)==v:
      c2+=1
if c1==2 and c2==2:
  print('yes')
else:
  print('no')
