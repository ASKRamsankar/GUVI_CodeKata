
no=int(input())
for i in range(2,no):
  if no%i==0:
    print('yes')
    break
if i+1==no:
  print('no')
