s1,s2=input().split()
s1=list(s1)
s2=list(s2)
m=abs(len(s1)-len(s2))
i=0
j=0
while i<len(s1) and j<len(s2):
  if s1[i]==s2[j]:
    i+=1
    j+=1
  else:
    if len(s1)>len(s2):
      s1.pop(i)
    else:
      i+=1
      j+=1
      m+=1
print(m)
