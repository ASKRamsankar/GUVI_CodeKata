r=input()
v=0
i=0
while i<len(r):
  try:
    if r[i]=='I' and r[i+1]=='V':
      v+=4
      i+=2
      continue
  except:
    pass
  if r[i]=='I':
    v+=1
  elif r[i]=='II':
    v+=2
  elif r[i]=='III':
    v+=3
  elif r[i]=='V':
    v+=5
  elif r[i]=='X':
    v+=10
  i+=1
print(v)
