import os
with open(os.path.join(os.getcwd(),'example.txt'), 'r') as file:
    content = file.read() # read all texts from file
    print(content)