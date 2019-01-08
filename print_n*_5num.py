no=int(input())
l=[]
for i in range(1,6):
  l.append(i*no)
for i in range(0,len(l)-1):
  print(l[i],end=' ')
print(l[len(l)-1])
