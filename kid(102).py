import sys
for line in sys.stdin:
  no=int(line.strip())
  while no%2==0:
    no/=2
  print(int(no))
