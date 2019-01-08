no=input()
sum=0
for i in no:
  sum+=int(i)**len(no)
if sum==int(no):
  print('yes')
else:
  print('no')
