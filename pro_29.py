def digit_s(t):
  o=0
  for i in str(t):
    o+=int(i)
  return o
no=int(input())
c=0
out=[]
for i in range(0,101):
  if abs(no-i)+digit_s(no-i)==no:
      c+=1
      out.append(no-i)
print(c)
for i in out:
  print(i)
