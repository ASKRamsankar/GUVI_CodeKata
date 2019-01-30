n=int(input())
strings=input().split()
for i in range(len(strings)-1):
  if len(strings[i])>len(strings[i+1]):
    strings[i],strings[i+1]=strings[i+1],strings[i]
for i in range(len(strings)-1):
  if len(strings[i])==len(strings[i+1]):
    a=strings[i]
    b=strings[i+1]
    for j in range(len(strings[i])):
      if a[j]>b[j]:
        strings[i],strings[i+1]=strings[i+1],strings[i]
        break
print(' '.join(strings))
