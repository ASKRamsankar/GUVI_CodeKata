def avg(temp):
    s=0
    for i in temp:
        s+=i
    return (s/len(temp))

n=int(input())
a=list(map(int,input().split()))
for i in range(1,n):
    print(a[:i],a[i:])
    s1=avg(a[:i])
    s2=avg(a[i:])
    print(s1,s2)
    if s1==s2:
        print('yes')
        break
else:
    print('no')
    
