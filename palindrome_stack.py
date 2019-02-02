class stack:
  def __init__(self):
    self.st=[]
    self.top=-1
  def update(self,array):
    for i in array:
      self.st.append(i)
      self.top+=1
  def check(self,c):
    if c==self.st[self.top]:
      self.top-=1
      return True
    else:
      return False
s=stack()
string=input()
s.update(string)
for i in string:
  if not s.check(i):
    print('NO')
    break
else:
  print('YES')
