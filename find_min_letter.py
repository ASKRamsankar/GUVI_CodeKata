string=input()
s=[]
d={}
for i in string:
  if i not in d:
    d[i]=1
  else:
    d[i]+=1
m=min(d.values())
for i in d.keys():
  if d[i]==m and i!=' ':
    s.append(i)
print(' '.join(s))
