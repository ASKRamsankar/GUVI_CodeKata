from itertools import permutations 
l=list(input()) 
perm = permutations(l) 
array=[]  
for i in list(perm):
  s='' 
  for j in i:
    s+=j
  if s not in array:
    array.append(s)
    print(s)
