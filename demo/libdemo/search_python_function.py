# Syntax: python search_python_function.py function_name [startdir]

import sys
import os


def does_file_use_function_name(filename, function_name):
    with open(filename, "rt") as f:
        contents = f.read()
        name = function_name + "("
        if name in contents:
            return True
        else:
            return False


if len(sys.argv) < 2:
    print("Usage : python search_python_function.py  function_name  [startdir]")
    exit()

function_name = sys.argv[1]
if len(sys.argv) > 2:
    startdir = sys.argv[2]
else:
    startdir = os.getcwd()

files_generator = os.walk(startdir)

for dirname, folders, files in files_generator:
    for f in files:
        if f.endswith(".py"):
            filename = dirname + "\\" + f
            if does_file_use_function_name(filename, function_name):
                print(filename)
