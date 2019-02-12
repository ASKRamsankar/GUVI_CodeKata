n,m=map(int,input().split())
M=[]
for i in range(n):
  M.append(list(map(int,input().split())))
for i in range(n):
  for j in range(m-1):
    for k in range(m-j-1):
      if M[i][k]>M[i][k+1]:
        M[i][k],M[i][k+1]=M[i][k+1],M[i][k]

for k in range(m):
  for i in range(n-1):
    for j in range(n-i-1):
      if M[j][k]>M[j+1][k]:
        M[j][k],M[j+1][k]=M[j+1][k],M[j][k]
for i in M:
  print(*i)
