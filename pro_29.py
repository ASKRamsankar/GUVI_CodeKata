def digit_s(t):
  o=0
  t=str(t)
  for i in t:
    o+=int(i)
  return o
no=int(input())
c=0
out=[]
for i in range(1,101):
  if no-i>0 and (no-i)+digit_s(no-i)==no:
      c+=1
      out.append(abs(no-i))
print(c)
for i in out:
  print(i)
