n,k=map(int,input().split())
input()
N=list(map(int,input().split()))
K=list(map(int,input().split()))
s=''
for i in K:
  N.append(i)
  s+=str(max(N))+' '
print(s[:-1])
