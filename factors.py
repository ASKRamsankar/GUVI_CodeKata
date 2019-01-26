no=int(input())
factors='1 '
for i in range(2,no):
  if no%i==0:
    factors+=str(i)+' '
print(factors+str(no))
