def find(S,l,r):
  length=0
  m=0
  if S[l:r]==S[l:r][::-1]:
    m=len(S[l:r])
    l-=1
    r+=1
    while l>=0 and r<=len(s) and S[l:r]==S[l:r][::-1]:
      m+=2
      l-=1
      r+=1
    if m>length:
      length=m
  return length

s=input()
out=0
t=0
if s==s[::-1]:
  out=len(s)
else:
  for i in range(2,4):
    j=0
    while j+i<=len(s):
      t=find(s,j,i+j)
      j+=1
      if out<t:
        out=t
print(len(s)-out)
