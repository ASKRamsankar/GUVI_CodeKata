n,k=map(eval,input().split())
nos=list(map(int,input().split()))
for i in range(len(nos)-1):
  if nos[i]+nos[i+1]==k:
    print('yes')
    break
else:
  print('no')
