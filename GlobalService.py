import os
import time
from datetime import datetime

import Folder as FD
import File as F


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


def renameFolder(folder, newName):

    root = folder.path[:folder.path.rfind("\\")+1]
    os.rename(folder.path, f'{root}{newName}')
    print(f'New folder name : {newName}')


def renameDuplicatedFolderNames(listfolderpaths, listFolderNames):
    # list of tuple of name and path
    listNamePath = list(zip(listFolderNames, listfolderpaths))

    # count number of same folder names
    folderCountDict = {}
    for i in range(len(listFolderNames)):
        if listFolderNames[i] in folderCountDict:
            folderCountDict[listFolderNames[i]] += 1
        else:
            folderCountDict[listFolderNames[i]] = 1

    # find duplicated folders
    listDuplicatedFolderNamesDict = {}
    for k, v in folderCountDict.items():
        if int(v) > 1:
            listDuplicatedFolderNamesDict[k] = v
    # listDuplicatedFolderNamesDict = sorted(listDuplicatedFolderNamesDict)
    print(listDuplicatedFolderNamesDict)
    
    # delete non duplicated folders in listNamePath
    tmp = []
    for item in listNamePath:
        if item[0] in listDuplicatedFolderNamesDict:
            tmp.append(item)
    listNamePath = tmp
    listNamePath = sorted(listNamePath, key=lambda x: x[0])
    print(listNamePath)
    
    # 继续 : 遍历 并 实现改名。
    for namePath in listNamePath:
        pass
            
    
