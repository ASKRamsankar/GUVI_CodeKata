n,m=map(eval,input().split())
binM=[]
for i in range(n):
  binM.append(list(map(eval,input().split())))
col,row=1,1
for i in range(n):
  for j in range(m):
    if binM[i][j]==1:
      c=1
      r=1
      j1=j
      while j1<m and binM[i][j1]==1:
        j1+=1
        r+=1
      i1=i
      for k in range(r):
        if i1+1<n:
          if binM[i1][j:j+r]==binM[i1+1][j:j+r]:
            c+=1
            i1+=1
          else:
            break
        else:
          break
  if c>col:
    col=c
for i in range(col):
  out=[1]*col
  print(*out)  
