string=input()
flag1=0
flag2=0
for i in string:
  if i.isdigit() and flag1!=1:
    flag1=1
  elif i.isalpha() and flag2!=1:
    flag2=1
  if flag1==1 and flag2==1:
    break

if flag1==1 and flag2==1:
  print("Yes")
else:
  print("No")
