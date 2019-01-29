n=int(input())
strings=[]
for i in range(n):
    strings.append(sorted(input()))
count=[2,1,1,1,1]
c=0
name=['a','a','b','i','k','l']
for i in strings:
    if i==name:
        c+=1
print(c)
