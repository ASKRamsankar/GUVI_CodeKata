s=input()
p1,p2=0,0
d=1
for i in s:
  if i=='G':
    if d==1:
      p1+=1
    elif d==2:
      p2-=1
    elif d==3:
      p1-=1
    elif d==4:
      p2+=1
  elif i=='L':
    if d==4:
      d=1
    else:
      d+=1
  elif i=='R':
    if d==1:
      d=4
    else:
      d-=1
if p1==0 and p2==0:
  print('yes')
else:
  print('no')
