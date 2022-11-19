# encoding:utf-8
import GlobalService


# path = input()

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
path = r'D:\python\apps\manapic\img'
listNewFolderNames = GlobalService.creatFoldersByMonth(path)



