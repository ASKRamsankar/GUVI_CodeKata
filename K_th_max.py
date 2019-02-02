n,k=map(int,input().split())
nos=list(map(int,input().split()))
i=0
while i<(k-1):
  nos.pop(nos.index(max(nos)))
  i+=1
print(max(nos))
