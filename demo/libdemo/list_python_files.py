import os

files_generator = os.walk(r"c:\classroom\oct29\demo")

for dirname, folders, files in files_generator:
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
