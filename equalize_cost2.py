s1,s2=input().split()
s=0
if len(s1)>len(s2):
  s1,s2=s2,s1
i=0
while i<len(s1):
  s+=(ord(s2[i])-ord(s1[i]))
  i+=1
for i in range(i,len(s2)):
  s+=ord(s2[i])-ord('a')+1
print(s)
