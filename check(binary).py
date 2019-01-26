import sys
string=input()
for i in string:
  if i!='1' or i!='0':
    print('no')
    sys.exit()
print('yes')
