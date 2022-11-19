import os
import time
from datetime import datetime


import FolderClass as FD
import FileClass as F


def generatePath(root, name):
    return os.path.join(root, name)


def readPath(path):
    """_summary_

    Args:
        path (String): _description_

    Returns:
        Folder.Folder : _description_
    """
    if os.path.exists(path) == False:
        print("The path entered does not exist. Please retry.")
        return

    # folder.path
    folder = FD.Folder(path)

    # folder.name
    folder.name = path[path.rfind("\\"):][1:]

    # folder.createdTime
    folder.createdTime = time.ctime(os.path.getctime(path))
    folder.createdTime = datetime.strptime(
        folder.createdTime, "%a %b %d %H:%M:%S %Y").strftime('%Y-%m-%d %H:%M:%S')

    # folder.lastModificationTime
    folder.lastModificationTime = time.ctime(os.path.getmtime(path))
    folder.lastModificationTime = datetime.strptime(
        folder.lastModificationTime, "%a %b %d %H:%M:%S %Y").strftime('%Y-%m-%d %H:%M:%S')

    # folder.listRootFiles = []
    # folder.listRootFoldersPaths = []
    # folder.listRootFoldersNames = []
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            folder.listRootFiles.append(item)
        elif os.path.isdir(os.path.join(path, item)):
            folder.listRootFoldersPaths.append(os.path.join(path, item))
            folder.listRootFoldersNames.append(item)
        else:
            print("Item is neither file nor dir. That should not exist.")

    # folder.size
    # folder.listAllFiles = []
    # folder.listAllFoldersPaths = []
    # folder.listAllFoldersNames = []
    for root, dirs, files in os.walk(path):
        for name in files:
            folder.size += os.path.getsize(os.path.join(root, name))
            folder.listAllFiles.append(name)
        for name in dirs:
            folder.listAllFoldersPaths.append(os.path.join(root, name))
            folder.listAllFoldersNames.append(name)

    return folder


def readFile(filePath):
    """_summary_

    Args:
        filePath (String): _description_

    Returns:
        File.File: _description_
    """
    return F.File(filePath)


def rename(path, newName):
    try:
        root = path[:path.rfind("\\")+1]
        os.rename(path, f'{root}{newName}')
        return f'SUCCESS \n New name : {newName}'
    except:
        print('An exception occurred')
        return f'FAILURE \n An exception occurred'


def checkDuplicatedFolderNamesExist(path):
    folder = readPath(path)
    listFolderNames = folder.listAllFoldersNames
    if len(set(listFolderNames)) != len(listFolderNames):
        print(f"### Path : {path} \n Duplicated folder names EXIST.")
        return True
    else:
        print(f"### Path : {path} \n Duplicated folder names DO NOT EXIST.")
        return False


def renameDuplicatedFolderNames(path):
    # readPath
    folder = readPath(path)
    listFolderNames = folder.listAllFoldersNames
    listfolderpaths = folder.listAllFoldersPaths
    # list of tuple of name and path
    listNamePath = list(zip(listFolderNames, listfolderpaths))

    # count number of same folder names and rename duplicated folders
    folderCountDict = {}
    for i in range(len(listFolderNames)):
        name = listFolderNames[i]
        if name not in folderCountDict:
            folderCountDict[name] = 0
        else:
            folderCountDict[name] += 1
            test = rename(listfolderpaths[i],
                          f'{name}({folderCountDict[name]})')
            print(f'Renaming \'{listfolderpaths[i]}\' : {test}')


def creatFoldersByMonth(path):
    """count creattion dates of photos in root path and create folders 
    with the format yyyy-mm

    Args:
        path (str): _description_
    """    
    print("creatFoldersByMonth")
