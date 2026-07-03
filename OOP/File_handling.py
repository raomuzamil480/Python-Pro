# file dedection
# import os
#
# file = "file.txt"
#
# if os.path.exists(file):
#     print('Yes file exist :')
#     if os.path.isfile(file):
#         print('Is file')
#     elif os.path.isdir(file):
#         print('Is dir')
#
# else:
#
#     print("Noooo")

#========================Write File

file_txt='i live lahore pakistan'
file_name='i.txt'
with open(file=file_name,mode='w') as file:
    file.write(file_txt)
    print(f'Created file {file_name}')
#=========================================JSON
import json
file_json={
    "name":"Rao",
    "age":"21"
}
fi_path='j.json'
try:
    with open(file=fi_path,mode='w') as file:
        json.dump(file_json,file,indent=5)
        print(f"create succesful {file_json}")
except FileExistsError:
    print("Already exist:")

#===================================TASK to Muzamil creta a .csv file like import csv

