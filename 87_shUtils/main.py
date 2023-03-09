import shutil
import os

# shutil.copy('main.py', 'main2.py')                               #copy file
# shutil.copytree('folder1', 'myfolder1')                      # copy folder  
# shutil.move('folder1/folder3/myfile2.txt', 'paras.txt')      #move file from folder
# shutil.rmtree('myfolder1')                                              #delete folder


# How to delete a file(you can't delete a file in shutil you have to delete it via OS module)
os.remove('paras.txt')