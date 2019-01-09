n,k=input().split()
k=int(k)
m=1000000
for i in range(len(n)-k):
    if int(n[i:i+k])<m:
        m=int(n[i:i+k])
print(m)    
