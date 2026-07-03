# file dedection
import os

file = "file.txt"

if os.path.exists(file):
    print('Yes file exist :')
    if os.path.isfile(file):
        print('Is file')
    elif os.path.isdir(file):
        print('Is dir')

else:

    print("Noooo")
