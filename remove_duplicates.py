string=input()
t=[]
for i in string:
  if i not in t:
    t.append(i)
print(''.join(t))
