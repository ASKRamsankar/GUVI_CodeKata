n=int(input())
nos=list(map(int,input().split()))
s=[]
for i in range(0,n-1):
  if max(nos[i+1:])<nos[i]:
    s.append(nos[i])
s.append(nos[i+1])
print(*s)
print(max(nos))
