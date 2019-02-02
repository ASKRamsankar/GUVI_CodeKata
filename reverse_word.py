string=input().split()
for i in range(len(string)):
  string[i]=string[i][::-1]
print(*string)
