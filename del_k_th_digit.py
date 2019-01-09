n,k=input().split()
k=len(n)-int(k)
m=100000000000000000000000000000000
if k==0:
    print(n)
else:
    for i in range(len(n)-k):
        if int(n[i:i+k])<m:
            m=int(n[i:i+k])
    print(m)    
