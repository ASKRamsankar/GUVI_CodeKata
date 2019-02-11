l,k=input().split()
l=list(l)
k=int(k)
for i in range(k):
    t=l.pop(len(l)-1)
    l.insert(0,t)
print(''.join(l))
