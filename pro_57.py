A,B=input().split()
for i in range(0,len(A)-1):
  if A[i:i+2] in B:
    print('yes')
    break
else:
  print('no')
