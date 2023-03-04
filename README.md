# manapic
A little program reads photo ExifTags and regroup them by month of year.


### TODO
1.debug : ImageService.renamePhotoNames(path) ==> wrong date

2.Optimize : GlobalService.createFoldersByDay(path) and GlobalService.remove_files_to_folder_by_creation_day(path) ==> do not need to verify if a file is a photo or video, read exiftag or file.createdTime


### architecture

OOP？

## OOP
# models
1.Folder

2.File
    ####重写？？？


# services
3.GlobalService()
    def progress_bar(count, total, status='')
    def generateLocation(root, name)
    def readPath(path): return Folder
    def readFile(fileAddress): return File
    def renameFolder(folder):
    def renameDuplicatedFolderNames(path)
    def checkDuplicatedFolderNames(path)
    def creatFoldersByMonth(path)

    def modifyFolderName(path)
    def moveFoldersToRoot(listPaths):
        while (checkSubFoldersExist())

    def initFolder(folder):
    def initFile(path):

    def createFoldersByDay(path)
    def createFoldersByMonth(path)

    def remove_files_to_folder_by_creation_day(path)

4.ImageService
    def readImg(imgPath)
    def renamePhotoNames(path)
    def get_video_info(video_file)
    def get_video_creation_time(video_file)



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

