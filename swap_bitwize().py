#swap
a,b=map(int,input().split(' '))
a=a^b
b=a^b
a=a^b
print(str(a)+' '+str(b))
