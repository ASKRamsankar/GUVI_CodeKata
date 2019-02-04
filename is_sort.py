n=int(input())
nos=list(map(eval,input().split()))
if nos==sorted(nos):
  print('yes')
else:
  print('no')
