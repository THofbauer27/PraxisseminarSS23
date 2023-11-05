import os

#input what the new class should be
print('Newclass')
newClass = input()

#get all data in this file.
dir_path = os.getcwd()
res = ''

#go through all .txt Files in this folder and exchange everything befor the first Space with new class.
for path in os.listdir(dir_path)
    if os.path.isfile(os.path.join(dir_path, path)):
      res = path
      if res[-4:] == '.txt':
          print(res)
          file1 = open("./"+res,"r")
          content = file1.read()
          file1.close()
          file1 = open("./"+res,"w")
          if content.split(" ", 1)[0] != "":
            file1.write(newClass+' '+content.split(" ", 1)[1]) 
          
          file1.close()

