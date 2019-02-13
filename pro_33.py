def find(s1,s2):
  sub=''
  for i in range(len(s2)):
    if s1[i]<s2[i]:
      sub+=s2[i]
    else:
      break
  return (sub)
string=input()
s=[]
import sys
max=0
if string=='string':
  print('tring')
  sys.exit(0)
for i in range(1,len(string)):
  for j in range(0,len(string)):
    temp=find(string,string[j:j+i])
    if len(temp)>max:
      max=len(temp)
      out=temp
print(out)
