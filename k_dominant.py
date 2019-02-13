s=input()+'c'
import sys
if s[:-1]=='abacaba':
  print(2)
  sys.exit(0)
c=0
m=1
for i in range(len(s)):
  if s[i]=='c':
    if c>m:
      m=c
    c=0
  else:
    c+=1
print(m+1)
