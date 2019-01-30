n=int(input())
nos=list(map(int,input().split()))
for i in nos:
  if i<=0:
    print(i,end=' ')
    print(abs(i))
    break
