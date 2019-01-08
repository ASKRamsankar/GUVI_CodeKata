start,end=map(int,input().split())
if start%2==0:
    start+=1
else:
    start+=2
while start<end:
    print(start,end=' ')
    start+=2
