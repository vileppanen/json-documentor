import json
import os
from lib.object_documentor import (
    documentize_object,
    documentize_prop,
    documentize_array,
)

file_name = input("Specify MD to convert: ")

file = open(file_name)

data = file.readlines()
# Iterating through the json
# list
xls_lines = []
for i in data:
    xls_lines.append(i.replace(" |", "\t"))
# Closing file
file.close()


# Write output XLS to file
directory = "./output-xls"

if not os.path.exists(directory):
    os.makedirs(directory)

file1 = open(directory + "/" + file_name + ".xls", "w+")
file1.writelines(xls_lines)
file1.close()
