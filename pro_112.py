import os 
import shutil
source_dir = "C:/Users/Admin/Downloads"
destination_dir = "C:/python programes"
list_of_files = os.listdir(source_dir)
for file in list_of_files:
    name,extension = os.path.splitext(file)
    print(name)
    print(extension)
if os.path.exists(path2):
    print("moving " + file_name + ".....")

    shutil.move(path1,path2)
else:
 os.makedirs(path2)
 print("moving" + file_name + ".....")
 shutil.move(path1,path3)    