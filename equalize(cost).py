s1,s2=input().split()
m=len(s2)
i=0
while i<len(s1):
  if s1[i]==s2[i]:
    m-=1
  i+=1
print(m)
