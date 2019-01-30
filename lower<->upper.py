string=input()
s=''
for i in string:
  if i.upper()==i:
    s+=i.lower()
  else:
    s+=i.upper()
print(s)
