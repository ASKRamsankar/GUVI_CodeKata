n,k=map(eval,input().split())
stu=list(map(int,input().split()))
i=0
c=0
while i<len(stu):
  if stu[i]+k<=5:
    c+=1
  i+=1
print(c//3)
