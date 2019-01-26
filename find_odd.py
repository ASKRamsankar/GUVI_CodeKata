no=input()
o=''
for i in no:
  if int(i)%2!=0:
    o+=i+' '
print(o[:-1])
