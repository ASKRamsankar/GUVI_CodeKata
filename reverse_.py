n=eval(input())
nos=list(map(eval,input().split()))
s=''
for i in range(1,len(nos)+1):
  s+=str(nos[-i])+'->'
print(s[:-2])
