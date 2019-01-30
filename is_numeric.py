string=input()
for i in string:
  if not i.isdigit():
    print('no')
    break
else:
  print('yes')
