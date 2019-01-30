l=[]
for i in range(3):
  x,y=map(int,input().split())
  l.append((x,y))
if (l[0][0]==l[1][0]) and (l[1][0]==l[2][0]):
  print('yes')
elif (l[0][1]==l[1][1]) and (l[1][1]==l[2][1]):
  print('yes')
elif (l[0][0]==l[0][1]) and (l[1][0]==l[1][1]) and (l[2][0]==l[2][1]):
  print('yes')
else:
  print('no')
