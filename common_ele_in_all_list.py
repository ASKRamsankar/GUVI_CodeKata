n,k=map(int,input().split())
n_l=[]
o=''
for i in range(n):
  n_l.append(list(map(int,input().split())))
for i in range(k):
  flag=0
  for j in range(1,n):
    if n_l[0][i] in n_l[j]:
      i1,j1=0,i
      flag+=1
  if flag==n-1:
    o+=str(n_l[0][i])+' '
print(o[:-1])
