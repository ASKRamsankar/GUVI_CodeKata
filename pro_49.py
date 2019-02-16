a=input()
b=input()
A=[]
s=''
for i in range(len(a)):
  if a[i] not in A:
    s+=a[i]
    A.append(a[i])
c=0
c=len(a)//len(s)
o=1
for i in range(2,c+1):
  if c%i==0:
    o+=1
print(o)
