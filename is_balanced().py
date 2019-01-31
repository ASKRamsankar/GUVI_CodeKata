string=input()
c=0
for i in string:
  if i=='(':
    c+=1
  elif i==')':
    c-=1
if c==0:
  print('yes')
else:
  print('no')
