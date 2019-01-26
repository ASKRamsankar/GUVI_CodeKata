import sys
string=input()
for i in range(len(string)):
    if string[i]=='1' or string[i]=='0':
      continue
    else:
      print('no')
      sys.exit(0)
print('yes')
