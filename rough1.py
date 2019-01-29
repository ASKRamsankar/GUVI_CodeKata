n,k=map(int,input().split())
nos=list(map(int,input().split()))
for i in range(k-1):
  nos.remove(min(nos))
print(min(nos))
