from genericpath import isdir, isfile
import os
import time 


# path = "./img"
# files = os.listdir(path)
# # print(files)
# fileNames = []

def readFilesNames(path):
    if os.path.exists(path) == False:
        return "The path entered does not exist. Please retry."
    result = os.listdir(path)
    # print(result)
    return result


def explorFiles(path):
    '''
    fonction to show path infos
    '''
    if os.path.exists(path) == False:
        return "The path entered does not exist. Please retry."
    size = 0
    getTime = f'Last modification time : {time.ctime(os.path.getmtime(path))}'
    numFiles = 0
    numDirs = 0
    listFiles = []
    listDirs = []
    for root, dirs, files in os.walk(path):
        for name in files :
            size += os.path.getsize(os.path.join(root, name)) / 1024**2
            listFiles.append(name)
        for name in dirs:
            listDirs.append(os.path.join(root, name))
    size = f'Folder size : {round(size, 1)}mo'
    numFiles = f'Folder has {len(listFiles)} files.'
    numDirs = f'Folder has {len(listDirs)} folders.'
    listFiles = f'List of files : \n {listFiles}'
    listDirs = f'List of folders : \n {listDirs}'
    print(f'{size}\n{getTime}\n{numFiles}\n{numDirs}\n{listFiles}\n{listDirs}')




explorFiles("./img")
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


    





