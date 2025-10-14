import shutil
import os
import time

### gett current folder path
folder_path = os.getcwd()
## go back one folder
os.chdir("..")
## update the folder path
folder_path = os.getcwd()
# go to needed folder with the offsets
offsets_place = folder_path + "\\json converter to py\\dumper\\output"
## .lnk because its a shorcut to the program
program_placement = folder_path + "\\json converter to py\\dumper\\json-dumper.exe.lnk"
json_converter_path = folder_path + "\\json converter to py"

##delete the previous offsets
try:
    shutil.rmtree(offsets_place)
except:
    pass

#remove the old json files
try:
    os.remove(json_converter_path + "\\client_dll.json")
except:
    pass
try:
    os.remove(json_converter_path + "\\offsets.json")
except:
    pass

## start the dumper
os.chdir(".\\json converter to py\\dumper")
os.startfile(program_placement)
## just so it wont give an error if the offsets folder is not created yet
time.sleep(3)


print(offsets_place)

## client_dll.json && offsets.json placements
client_dll_path = folder_path + "\\json converter to py\\dumper\\output\\client_dll.json"
offsets_path = folder_path + "\\json converter to py\\dumper\\output\\offsets.json"
## move the new offsets to the json converter to py folder
shutil.move(client_dll_path, json_converter_path)
shutil.move(offsets_path, json_converter_path)

#start the json converter to py script
json_converter_program = folder_path + "\\json converter to py\\json_convert_V3.py"
# go back to the main folder - so it will find client_dll.json and offsets.json
os.chdir("..")
os.startfile(json_converter_program)

os.chdir("..")
try:
    os.remove("offsets.py")
    os.remove("client.py")
except:
    pass

# move the new offsets to the main folder
shutil.move(json_converter_path + "\\offsets.py", folder_path)
shutil.move(json_converter_path + "\\client.py", folder_path)
print("done")
time.sleep(1)


