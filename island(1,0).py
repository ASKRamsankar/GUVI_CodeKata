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
      try:
        if M[i-1][j]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M[i+1][j]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M[i][j-1]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M[i][j+1]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M[i-1][j-1]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M[i-1][j+1]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M[i+1][j-1]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M[i+1][j+1]==0:
          f+=1
      except IndexError:
        f+=1
    if f==8:
      c+=1

print(c)
