# from genericpath import isdir, isfile
import os
import time 

# funtion reads path and return lists of files, paths and folder names
def readPath(path):
    if os.path.exists(path) == False:
        return "The path entered does not exist. Please retry."
    size = 0
    lastModifiedTime = time.ctime(os.path.getmtime(path))
    listFiles = []
    listPaths = []
    listFolderNames = []
    for root, dirs, files in os.walk(path):
        for name in files :
            size += os.path.getsize(os.path.join(root, name)) / 1024**2
            listFiles.append(name)
        for name in dirs:
            listPaths.append(os.path.join(root, name))
            listFolderNames.append(name)
    
    numFiles = len(listFiles)
    numFolders = len(listPaths)
    
    sizeStr = f'Folder size : {round(size, 1)}mo'
    lastModifiedTimeStr = f'Last modification time : {lastModifiedTime}'
    numFilesStr = f'There are {numFiles} files.'
    numPathsStr = f'There are {numFolders} paths.'
    listFilesStr = f'List of files : \n {listFiles}'
    listPathsStr = f'List of paths : \n {listPaths}'
    listFolderNamesStr = f'List of folders : \n {listFolderNames}'
    toString = (f'##Path : {path}\n{sizeStr}\n{lastModifiedTimeStr}\n{numFilesStr}\n{numPathsStr}\n{listFilesStr}\n{listPathsStr}\n{listFolderNamesStr}')
    return  toString, listFiles, listPaths, listFolderNames


def explorPath(path):
    return readPath(path)[0]

def getListFiles(path):
    return readPath(path)[1]
       
def getListPaths(path):
    return readPath(path)[2]

def getListFolderNames(path):
    return readPath(path)[3]




# ==note==
# explorPath("./img")
# print(os.path.getsize("./img"))
# print(os.listdir("./img"))
# print(os.walk("./img"))

# size
# fileSize = os.path.getsize("./img/00000PORTRAIT_00000_BURST20190422122038492.jpg") / (1024**2)
# print(fileSize)

# Scandir = os.scandir('./img')
# for file in Scandir:
#     print(file)

# os.walk()
# listFiles = []
# for root, dirs, files in os.walk("./img"):
#     for name in files:
#         # path = os.path.join(root, name)
#         listFiles.append(name)
# print(listFiles)
    

# ==time package==
# print(time.gmtime())    
# print(time.sleep())

# secend to time string
# t = 1666213664.631179
# tTime = time.ctime(t)
# print(tTime)


    





