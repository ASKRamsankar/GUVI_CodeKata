string=input()
c=0
ind=len(string)
i=0
while i<len(string):
  if string[i]==' ':
    string=string[:i]+string[i+1:]
    continue
  i+=1
print(string)

