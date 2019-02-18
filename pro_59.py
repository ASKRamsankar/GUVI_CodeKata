scale=input()+input()
l_scale,r_scale=scale.split('|')
if len(l_scale)==len(r_scale):
  print(scale)
else:
  print('impossible')
