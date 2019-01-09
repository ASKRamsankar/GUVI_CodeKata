import sys
l=[]
n=int(input())
def find_common(s1,s2):
    i=0
    com=''
    while i<len(s1):
      j=0
      while j<len(s2):
        if s1[i]==s2[j]:
          s=s1[i]
          i1=i+1
          j1=j+1
          while i1<len(s1) and j1<len(s2) and s1[i1]==s2[j1]:
            s+=s1[i1]
            i1+=1
            j1+=1
          if len(com)<len(s):
            com=s
            s=''
        j+=1
      i+=1
    return com


for i in range(n):
    l.append(input())
if len(l)==1:
    print(l[0])
    sys.exit()
common=find_common(l[0],l[1])
for i in range(2,n):
    common=find_common(common,l[i])

print(common)
    
