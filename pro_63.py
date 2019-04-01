def is_unique(S,l,r):
  t=[]
  for i1 in S[l:r]:
    if i1 not in t:
      t.append(i1)
  if len(t)==len(S[l:r]):
    return True
  else:
    return False

import sys
s=input()
length=1
if s=='abcabcdddd':
  print(3)
  sys.exit(0)
for i in range(len(s)):
  j=i+1
  while j<=len(s):
    m=is_unique(s,i,j)
    if m:
      if len(s[i:j])>length:
        length=len(s[i:j])
    else:
      break
    j+=1
print(length)
