s1,s2=input().split()
i=0
j=0
c=0
while i<len(s1) and j<len(s2):
  if s1[i]!=s2[i]:
    c+=1
  i+=1
  j+=1
if c==0 and len(s1)-len(s2)==1:
  print('yes')
if c<=1:
  print('yes')
else:
  print('no')
