s=input()
c=0
for i in s:
  if not (i.isdigit() or i.isalpha() or i==' '):
    c+=1
print(c)
