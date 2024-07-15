import os

base_path = ".\\temp"

# get current dir
print(os.getcwd()) 

# check path exists
print(os.path.exists(base_path))

# auto create folder
if not os.path.exists(base_path): # if the pat is not exist
    print("Create path")
    os.mkdir(base_path) # than, make the directory

# execute system command
os.system("dir") # "ls" in Linux/Mac

# list files in dir
files = os.listdir(base_path)
print("[Files in temp] ", files)

# concat the path (join)
for file_name in files:
    file_path = os.path.join(base_path,file_name)
    print(file_path)

# print file nums
print("Total",len(files), "files in this folder")