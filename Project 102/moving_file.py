import os
import shutil

from_dir = "/Users/dainorag/Downloads/"
to_dir = "/Applications"
list_of_files = os.listdir(from_dir)
print(os.path.exists(from_dir))
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == "": continue
    if extension in [".txt",".pdf"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + "/" + file_name
        if os.path.exists(path2): 
            shutil.move(path1,path3)
            print("moving" + file_name + "...")
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving" + file_name + "...")
            