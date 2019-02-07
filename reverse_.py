#dfghj
n=eval(input())
nos=list(map(eval,input().split()))
s=[]
for i in range(1,len(nos)+1):
  s.append(str(nos[-i]))
print('->'.join(s))
