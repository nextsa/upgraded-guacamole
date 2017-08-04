import yaml
import shutil
import re
import glob
print("Project folder:")
projectFolder = input()
print("Copying folder:")
copyingFolder = input()
#projectFolder = r"D:/project/"
#copyingFolder = r"D:/test/"

with open("dihmi_resources.yaml", 'r', encoding='utf-8') as stream:
    try:
        data_loaded = yaml.load(stream)
        for i in data_loaded['additionalIntegrity']:
            (left, right) = i.split(',')
            (something, key) = right.split(r'hmi/')
            copyingPath = copyingFolder + str(key) # Place to copy
            if "*" in left:
                (path, files) = left.split("/*")
                projectPath = projectFolder + str(left)
                if "." in files:
                    for f in glob.glob(projectPath):
                        shutil.copy2(f, copyingPath)
                else:
                    for f in glob.glob(projectPath):
                        shutil.copy2(f, copyingPath)
            else:
                projectPath = projectFolder + str(left)
                shutil.copy(projectPath, copyingPath)

    except yaml.YAMLError as exc:
        print(exc)
