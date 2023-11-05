#This programm gets all Files of the type .JPG and turns them into .jpg files
import os
#get the location of the programm
dir_path = os.getcwd()

# check if there are JPG files in the folder and Change them to jpg
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
      res = path
      if res[-4:] == '.JPG':
        old_name = dir_path + "/" + path
        new_name = dir_path + "/" + path[:-4] + ".jpg"
        os.rename(old_name, new_name)
