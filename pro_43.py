def find(temp,d):
  avail=sorted(d.keys())
  for i in range(len(avail)):
    if temp in avail:
      temp+=1
    else:
      break
  return temp
n=int(input())
a=list(map(int,input().split()))
d={}
c=0
for i in range(n):
  if a[i] not in d.keys():
    d[a[i]]=1
  else:
    d[a[i]]+=1
temp=1
temp=find(temp,d)
ins=[]
for i in range(n):
  if d[a[i]]==1:
    ins.append(a[i])
for i in range(n):
  if d[a[i]]==1:
    ins.append(a[i])
  elif a[i] in ins:
    d[a[i]]-=1
    a[i]=temp
    ins.append(temp)
    d[temp]=1
    temp=find(temp+1,d)
    c+=1
  elif a[i]>temp:
    d[a[i]]-=1
    a[i]=temp
    ins.append(temp)
    d[temp]=1
    temp=find(temp+1,d)
    c+=1
  else:
    ins.append(a[i])
print(c)
print(*a)
