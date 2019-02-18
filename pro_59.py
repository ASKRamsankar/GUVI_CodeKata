scale=input()
wei=input()
scale1=scale+wei
scale2=wei+scale

l_scale1,r_scale1=scale1.split('|')
l_scale2,r_scale2=scale2.split("|")
if len(l_scale1)==len(r_scale1):
  print(scale1)
elif len(l_scale2)==len(r_scale2):
  print(scale2)
else:
  print('impossible')
