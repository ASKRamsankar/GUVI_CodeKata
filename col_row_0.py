n,m=map(eval,input().split())
n_l=[]
for i in range(n):
  n_l.append(list(map(eval,input().split())))
for i in range(len(n_l)):
  for j in range(len(n_l[i])):
    if n_l[i][j]==0:
      for i2 in range(n):
        if n_l[i2][j]!=9:
          n_l[i2][j]=9
      for j2 in range(m):
        if n_l[i][j2]!=9:
          n_l[i][j2]=9
for i in range(len(n_l)):
  for j in range(len(n_l[i])):
    if n_l[i][j]==9:
      n_l[i][j]=0
  print(*n_l[i])
