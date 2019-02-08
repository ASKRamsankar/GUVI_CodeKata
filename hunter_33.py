string=input()
flag=0
c=0
m=0
for i in string:
  if i=='a' and flag==0:
      c+=1
      flag=1
  elif i=='b' and flag==1:
      c+=1
      flag=0
  else:
    if c>m:
      m=c
    flag=0
    c=0
else:
  if c>m:
    m=c
if m==1:
  print(m-1)
else:
  print(m)
