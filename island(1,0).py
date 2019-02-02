#island
n=int(input())
M=[]
c=0
for i in range(n):
  M.append(list(map(int,input().split())))
f=0
for i in range(len(M)):
  for j in range(len(M[0])):
    f=0
    if M[i][j]==1:
      if i-1<0:
        f+=1
      elif M[i-1][j]==0:
        f+=1
      if i+1>=len(M):
        f+=1
      elif M[i+1][j]==0:
        f+=1
      if j-1<0:
        f+=1
      elif M[i][j-1]==0:
        f+=1
      if j+1>=len(M):
        f+=1
      elif M[i][j+1]==0:
        f+=1
    if f==4:
      c+=1

print(c)
