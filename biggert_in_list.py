n=int(input())
nos=input().split()
no=[]
while len(nos)!=0:
    no.append(max(nos))
    nos.pop(nos.index(max(nos)))
print(''.join(no))
