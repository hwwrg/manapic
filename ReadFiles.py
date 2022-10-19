import os

path = "./img"
files = os.listdir(path)
# print(files)
fileNames = []

for file in files:
    if not os.path.isdir(file):
        fileNames.append(file)
        print(type(file))

print(fileNames)
print(type(fileNames))
