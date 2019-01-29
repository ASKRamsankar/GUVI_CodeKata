vow=['a','e','i','o','u']
n=int(input())
string=input()
s=''
i=0
while i<len(string):
    if string[i].lower() not in vow:
        s+=string[i]
    i+=1
print(s[::-1])
