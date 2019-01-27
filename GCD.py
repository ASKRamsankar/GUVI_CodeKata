#lfkdjsf;k
n1,n2=map(int,input().split())
flag=0
gcd=1
def find(n,m):
  global n1,n2,flag
  i=0
  for i in range(2,min(n,m)+1):
    if n%i==0 and m%i==0:
      n/=i
      n1=int(n)
      m/=i
      n2=int(m)
      return i
  else:
      flag=1
      #return (m*n)
      return 1

while flag!=1:
  gcd*=(find(n1,n2))
print(gcd)
