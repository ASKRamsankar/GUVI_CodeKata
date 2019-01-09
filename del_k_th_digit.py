n,k=input().split()
k=int(k)
min1=10000
def remove(inx):
    s=''
    for i in range(len(n)):
        if i<inx+k and i>=inx:
            continue
        else:
            s+=n[i]
    return s
for i in range(len(n)):
    value=remove(i)
    if min1>int(value):
        min1=int(value)
print(min1)
    
