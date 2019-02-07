string=input()
for i in range(0,len(string)+1):
  s1=string[:len(string)-i]
  s2=s1[::-1]
  if s1!=s2:
    print(s1)
    break
