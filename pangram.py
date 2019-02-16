string=input()
d={}
import sys
for i in string:
  if i!=' ':
    if i not in d.keys():
      d[i.lower()]=1
    else:
      d[i.lower()]+=1
if len(d)==26:
  print('yes')
else:
  print('no')
