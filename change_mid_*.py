string=input()
if len(string)%2==0:
  print(string[:int(len(string)/2)-1]+'**'+string[int(len(string)/2)+1:])
else:
  print(string[:int(len(string)/2)]+'*'+string[int(len(string)/2)+1:])
