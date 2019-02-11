from itertools import permutations
n=input()
s=list(permutations(n,len(n)))
j=0
strings=[]
for i in s:
  strings.append(''.join(i))

m=max(strings)
for i in strings:
  if i<m and i>n:
    m=i
if m==n:
  print('impossible')
else:
  print(m)
