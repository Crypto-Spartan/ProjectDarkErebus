import os

for (root,dirs,files) in os.walk('data', topdown=True):
  #root = root.split('/')
  print(root)
  print(dirs)
  print(files)
  print('--------------------------------------------------------------------------')