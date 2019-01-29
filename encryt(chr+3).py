string=input()
output=''
for i in string:
    if (ord(i)+3)>ord('Z'):
        output+=chr((ord(i)+3-ord('Z'))+ord('A')-1)
    else:
        output+=chr(ord(i)+3)
print(output)
