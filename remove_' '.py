string=input()
c=0
ind=len(string)
i=0
while i<len(string):
  if string[i]==' ':
    ind=i
    while i<len(string) and string[i]==' ':
      c+=1
      i+=1
    if c==1:
      c=0
  i+=1
  string=string[:ind]+string[ind+c:]
print(string)
