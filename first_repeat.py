n=int(input())
nos=input().split()
no=[]
for i in nos:
  if i not in no:
    no.append(i)
  else:
    print(i)
    break
else:
  print('unique')
