s1=input()
s2=input()
out=''
for i in range(len(s2)):
  t=ord(s2[i])-96
  t=t+ord(s1[i])
  if t>ord('z'):
    t=t-ord('z')
    t=t+96
  out+=chr(t)
print(out)
