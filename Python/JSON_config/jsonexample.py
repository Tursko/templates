#!/usr/bin/python3
import json

list_data=[]
imported_data=[]

dict_data={}

list_data.append("first")
list_data.append("second")
dict_data["a"]="first"
dict_data["b"]="second"

print("ORIGINAL list_data")
print(list_data)
print("ORIGINAL dict_data")
print(dict_data)
print("")
with open('list_example.json', 'w') as outfile:
    json.dump(list_data, outfile)

try:
    with open('list_example.json') as json_data:
        imported_data = json.load(json_data)
    print("new imported_data")
    print(imported_data)
except:
    print("Error: no json file found!")

########################################################
imported_data=[] #clearing it for second example

with open('dict_example.json', 'w') as outfile:
    json.dump(dict_data, outfile)

try:
    with open('dict_example.json') as json_data:
        imported_data = json.load(json_data)
    print("new imported_data")
    print(imported_data)
except:
    print("Error: no json file found!")