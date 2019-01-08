start,end=map(int,input().split())
l=[]
if start%2==0:
    start+=1
else:
    start+=2
while start<end:
    l.append(start)
    start+=2
for i in range(len(l)-1):
    print(l[i],end=' ')
print(l[len(l)-1])
