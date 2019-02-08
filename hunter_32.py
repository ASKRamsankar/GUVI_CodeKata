def fetch(array):
  temp=[]
  for i in range(1,len(array),2):
    temp.append(array[i])
  return temp

n=int(input())
arr=list(map(eval,input().split()))
dup=fetch(arr)
while len(dup)>1:
  dup=fetch(dup)
print(arr.index(dup[0]))
