#ghjk
flag=0

def find(n,m):
    global flag
    N,M=n,m
    i=0
    for i in range(2,min(n,m)+1):
      if n%i==0 and m%i==0:
        n/=i
        N=int(n)
        m/=i
        M=int(m)
        return (i,N,M)
    else:
      flag=1
      return (1,N,M)

def GCD(array,l,r):
  global flag
  gcd=1
  n1=array[l-1]
  n2=array[l]
  #print(n1,n2)
  if min(n1,n2)==1:
    gcd=1
  else:
    while flag!=1:
      t,n1,n2=find(n1,n2)
      gcd*=t
    #print(gcd)
    flag=0
  for i in range(l+1,r):
    n1=gcd
    n2=array[i]
    gcd=1
    #print(n1,n2)
    if min(n1,n2)==1:
      gcd=1
    else:
      while flag!=1:
        t,n1,n2=find(n1,n2)
        gcd*=t
      #print(gcd)
      flag=0
  return gcd    
    

n,k=map(int,input().split())
nos=list(map(int,input().split()))
bound=[]
for i in range(k):
  bound.append(list(map(int,input().split())))

for i in range(len(bound)):
  if bound[i][0]==bound[i][1]:
    print(nos[bound[i][0]-1])
  else:
    print(GCD(nos,bound[i][0],bound[i][1]))
