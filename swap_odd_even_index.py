s1=list(input())
j=1
i=0
while j<len(s1):
  s1[i],s1[j]=s1[j],s1[i]
  i+=2
  j+=2
print(''.join(s1))
