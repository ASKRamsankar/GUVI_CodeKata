s1,s2=input().split()
if len(s1)>len(s2):
  m=len(s1)
else:
  m=len(s2)
i=0
while i<len(s1) and i<len(s2):
  if s1[i]==s2[i]:
    m-=1
  i+=1
print(m)
