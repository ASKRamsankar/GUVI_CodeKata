d={}
s1,s2=input().split()
for i in range(len(s1)):
  if len(s1)!=len(s2):
    break
  if s1[i] not in d:
    d[s1[i]]=s2[i]
  elif d[s1[i]]!=s2[i]:
    print('no')
    break
else:
  if i+1==len(s1):
    print('yes')
