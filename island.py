n=int(input())
M=[]
for i in range(n):
  M.append(list(map(int,input().split())))
print(M)
for i in range(len(M)):
  for j in range(len(M[0])):
    if M[i][j]==1:
      try:
        if M[i-1][j]==0:
          f+=1
      except:
        pass
      try:
        if M[i+1][j]==0:
          f+=1
      except:
        pass
      try:
        if M[i][j-1]==0:
          f+=1
      except:
        pass
      try:
        if M[i][j+1]==0:
          f+=1
      except:
        pass
    if f==4:
      print(1)
    
