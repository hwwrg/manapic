# manapic
A little program reads photo ExifTags and regroup them by month of year.


### architecture

OOP？

## OOP
# models
1.Folder

2.File


3.GlobalService()
    def generatePath(root, name)
    def readPath(path): return Folder
    def readFile(fileAddress): return File
    def renameFolder(folder):
    def renameDuplicatedFolderNames(path)

    def checkDuplicatedFolderNames(path)
    def creatFolder(path=none, listPaths[])
    def moveFoldersToRoot(listPaths):
        while (checkSubFoldersExist())
    def creatSingleFolder(path, folderName)
    def creatMultiFolders({} NewFolders)

    def initFolder(folder):
    def initFile(path):



## should have
    -GC/object destroction
    -processing bar
    -ImgService



## without OOP : abandened
1.PathService(root)
    -explorPath()
    -getListFiles()
    -getListPaths()
    -getListFolderNames()

2.FileService(path)
    -getCreatedDate() : max number of created date

3.FolderService(folder, createdDate)
    -rename()

4.GlobalService()
    -renameDuplicatedFolderNames(listFolderNames)
    -moveFoldersToRoot

