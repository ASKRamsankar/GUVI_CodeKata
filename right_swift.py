n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    t=l.pop(len(l)-1)
    l.insert(0,t)
s=''
for i in l:
  s+=str(i)+' '
print(s[:-1])
