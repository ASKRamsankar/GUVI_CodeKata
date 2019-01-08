start,end=map(int,input().split())
if start%2==0:
    start+=2
else:
    start+=1
while start<end:
    print(start)
    start+=2
