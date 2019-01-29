def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
    
no=int(input())
output=''
for i in range(2,no+1):
    if no%i==0:
        if prime(i):
            output+=str(i)+' '
print(output[:-1])
