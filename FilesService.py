from genericpath import isdir, isfile
import os


# path = "./img"
# files = os.listdir(path)
# # print(files)
# fileNames = []

def readFilesNames(path):
    if os.path.exists(path) == False:
        return "The path entered does not exist. Please retry."
    result = os.listdir(path)
    print(result)
    return result


def explorFiles(path):
    if os.path.exists(path) == False:
        return "The path entered does not exist. Please retry."
    size = "Folder size : " + str(os.path.getsize(path))
    getTime = f'Last modification time : {os.path.getmtime(path)}'
    numFiles = 0
    numDirs = 0
    for file in readFilesNames(path):
        if os.path.isfile(f'{path}/{file}'):
            numFiles += 1
        elif os.path.isdir(f'{path}/{file}'):
            numDirs += 1
    numFiles = f'Folder has {numFiles} files.'
    numDirs = f'Folder has {numDirs} folders.'
    print(size, getTime, numFiles, numDirs)

readFilesNames("./img")
explorFiles("./img")
    
    


    





