from tkinter.font import names
import GlobalService
import ImageService
import FileClass


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

# ==is_image=
# root = r'D:\python\apps\manapic\imgOneFolder'
# img_name = 'ne2.jpg'
# file = GlobalService.generateLocation(root, img_name)
# print(GlobalService.is_image(file))


# ==createFoldersByMonth==
# path = r'D:\python\apps\manapic\imgOneFolder'
# listNewFolderNames = GlobalService.creatFoldersByMonth(path)
# print(listNewFolderNames)

# ==createFoldersByDay==

path = r'D:\照片备份\rx100 备份'
listNewFolderNames = GlobalService.createFoldersByDay(path)
print(listNewFolderNames)


# @@@@@@ ImageService @@@@@@
# ==getExifTags==
# root = r"D:\照片编辑\2023相册\12 - 副本"
# imgName = r"20221203_123043.JPG"
# imgPath = GlobalService.generatePath(root, imgName)
# test = ImageService.getExifTags(imgPath)
# print(test)

# ==renamePhoto==
# root = r'D:\照片编辑\2023相册\00'
# ImageService.renamePhotoNames(root)

