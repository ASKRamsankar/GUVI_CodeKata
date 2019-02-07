n=int(input())
nos=list(map(eval,input().split()))
bi=[]
for i in nos:
  bi.append('{:2b}'.format(i))
for i in range(len(bi)):
  c=0
  for j in bi[i]:
    if j=='1':
      c+=1
  bi[i]=c

for i in range(len(bi)-1):
  for j in range(0,len(bi)-i-1):
    if bi[j]<bi[j+1]:
      bi[j],bi[j+1]=bi[j+1],bi[j]
      nos[j],nos[j+1]=nos[j+1],nos[j]

for i in range(len(bi)-1):
  for j in range(0,len(bi)-i-1):
    if bi[j]==bi[j+1]:
      if nos[j]<nos[j+1]:
        nos[j],nos[j+1]=nos[j+1],nos[j]

for i in nos:
  print(i)
