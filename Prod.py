import GlobalService
import ImageService


# path = input()

# @@@@@@ GlobalService  @@@@@@
# ==readPath==
# path = r"D:\python\apps\manapic\img"
# f = GlobalService.readPath(path)
# print(f.path)

# ==readFile==
# root = "D:\python\/apps\manapic\img"
# name = "python.txt"
# filePath = GlobalService.generatePath(root, name)
# file = GlobalService.readFile(filePath)
# print(file.createdTime)
# print(file.lastModificationTime)

# ==rename==
# path = r'D:\python\apps\manapic\newImg'
# GlobalService.rename(path, "img")

# ==renameDuplicatedFolderNames==
# path = r'D:\python\apps\manapic\img'
# GlobalService.renameDuplicatedFolderNames(path)

# ==checkDuplicatedFolderNamesExist==
# path = r'D:\python\apps\manapic\img'
# duplicatedFolderNamesExist = GlobalService.checkDuplicatedFolderNamesExist(path)
# print(duplicatedFolderNamesExist)

# ==creatFoldersByMonth==
path = r'D:\python\apps\manapic\imgOneFolder'
listNewFolderNames = GlobalService.creatFoldersByMonth(path)
print(listNewFolderNames)



# @@@@@@ ImageService @@@@@@
# ==getExifTags==
# root = r"D:\python\apps\manapic\imgOneFolder"
# imgName = r"20220820_232743.JPG"
# imgPath = GlobalService.generatePath(root, imgName)
# test = ImageService.getExifTags(imgPath)
# print(test)

