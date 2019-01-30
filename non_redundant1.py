#dfgh
n=int(input())
string=list(map(int,input().split()))
num=[]
count=[]
for i in string:
    if i not in num:
        num.append(i)
        count.append(1)
    else:
        count[num.index(i)]+=1

print(num[count.index(1)]) 
