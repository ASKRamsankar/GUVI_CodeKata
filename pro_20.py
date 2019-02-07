n,k=map(eval,input().split())
coins=list(map(eval,input().split()))
count=0
while count!=k:
  c=int(n/max(coins))
  count+=(c*max(coins))
  n=n%max(coins)
  coins.remove(max(coins))
print(c)
