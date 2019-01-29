import sys
for line in sys.stdin:
  line=line.strip()
  if line=="Saturday" or line=="Sunday":
    print("yes")
  else:
    print("no")
