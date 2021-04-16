import json
import os
from lib.object_documentor import (
    documentize_object,
    documentize_prop,
    documentize_array,
)

file_name = input("Specify json to document: ")

file = open(file_name)

data = json.load(file)

# Iterating through the json
lines = [" Prop | Type | Description | Example \n", "----|----|----|----\n"]
for i in data:
    parents = (i,)
    if isinstance(data[i], dict):
        lines = lines + documentize_object(i, data[i], parents)
    elif isinstance(data[i], list):
        lines = lines + documentize_array(i, data[i], parents)
    else:
        lines = lines + documentize_prop(i, data[i])
file.close()

# Write output MD to file
directory = "./output-md"

if not os.path.exists(directory):
    os.makedirs(directory)
file1 = open(directory + "/" + file_name + ".md", "w+")
file1.writelines(lines)
file1.close()
