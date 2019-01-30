n=int(input())
strings=input().split()
for i in range(len(strings)):
  for j in range(0,n-i-1):
    if len(strings[j])>len(strings[j+1]):
      strings[j],strings[j+1]=strings[j+1],strings[j]

for i in range(len(strings)-1):
  if len(strings[i])==len(strings[i+1]):
    a=strings[i]
    b=strings[i+1]
    for j in range(len(strings[i])):
      if a[j]<b[j]:
        break
      elif a[j]>b[j]:
        strings[i],strings[i+1]=strings[i+1],strings[i]
        break
print(' '.join(strings))
