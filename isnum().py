s=input()
for i in s:
  if i.isdigit() or i=='.':
    flag=1
  else:
    flag=0
    break
if flag==1:
  print('yes')
else:
  print('No')
