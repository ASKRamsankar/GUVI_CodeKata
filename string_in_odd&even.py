string=input()
flag=0
o1=''
o2=''
for i in string:
  if flag==0:
    o1+=i
    flag=1
  else:
    o2+=i
    flag=0
print(o1+' '+o2)
