# manapic
A little program reads photo ExifTags and regroup them by month of year.


### architecture

OOP？

## OOP
# models
1.Folder
    path
    name
    size
    createdTime
    lastModificationTime
    listAllFiles
    listRootFiles
    listAllPaths
    listRootPaths
    listAllFolders
    listRootFolders

    def __ini__(self, root):
    def explorFolder(self):
    def rename(self, newName):
    


2.File
    path
    name
    size
    createdTime
    lastModificationTime

    def __ini__(self):
    def rename(self, newName):


3.GlobalService()
    def readPath(path): return Folder
    def readFile(fileAddress): return File
    def renameDuplicatedFolderNames(listFolderNames)
    def moveFoldersToRoot(listPaths)


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

