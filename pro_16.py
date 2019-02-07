n=int(input())
nos=list(map(eval,input().split()))
cdl=[1]*n
out=0
for i in range(n-1):
  for i in range(0,n-i-1):
    if nos[i]<nos[i+1]:
      cdl[i+1]=cdl[i]+1
    elif nos[i+1]<nos[i]:
      cdl[i]=cdl[i+1]+1
for i in range(len(cdl)):
  out+=cdl[i]
print(out)
