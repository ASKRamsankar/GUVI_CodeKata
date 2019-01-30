n=int(input())
nos=input().split()
no=[]
while len(nos)!=0:
  if max(nos) not in no:
    no.append(max(nos))
    nos.pop(nos.index(max(nos)))
  else:
    nos.pop(nos.index(max(nos)))
print(''.join(no))
