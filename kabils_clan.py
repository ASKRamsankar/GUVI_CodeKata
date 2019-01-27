import sys
for line in sys.stdin:
  n1,n2=map(int,line.split())
  print(abs(n1-n2))
