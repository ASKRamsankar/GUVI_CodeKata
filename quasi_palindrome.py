string=input()
c=0
for i in range(len(string)-1,-1,-1):
  if string[i]=='0':
    c+=1
  else:
    break
string=string[:-c]
if string==string[::-1]:
  print('yes')
else:
  print('no')
