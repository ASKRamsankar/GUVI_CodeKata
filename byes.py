import sys
n=int(input())
val=1
i=0
while val<n:
  if 2**i==n:
    print(0)
    sys.exit(0)
  val=2**i
  i+=1
print(n-int(val/2))
