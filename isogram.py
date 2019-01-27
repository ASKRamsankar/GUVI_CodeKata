import sys
for line in sys.stdin:
  l=[]
  for i in line:
    if i not in l:
      l.append(i)
    else:
      print('No')
      break
  if len(l)==len(line):
    print('Yes')
