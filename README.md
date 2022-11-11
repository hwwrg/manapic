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
    def explorPath(self):
    def rename(self, newName):
    


2.File
    path
    name
    size
    createdTime
    year
    month
    day
    lastModificationTime

    def __ini__(self):

3.GlobalService()
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

