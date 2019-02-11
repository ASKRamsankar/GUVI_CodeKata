n=input()
f=0
for i in range(1,len(n)):
  j=0
  while j<len(n) and len(n[:j]+n[j+i:])==len(n)-i:
    no=n[:j]+n[j+i:]
    no=int(no)
    if no>-1 and no%8==0:
      print('yes')
      f=1
      break
    j+=1
  if f==1:
    break
else:
  print('no')
