# encoding:utf-8
import GlobalService



# ==readPath==
# path = input()
# path = "./img"
# f = GlobalService.readPath(path)
# print(f.path)

# ==readFile==
# root = "D:\python\/apps\manapic\img"
# name = "python.txt"
# filePath = GlobalService.generatePath(root, name)
# file = GlobalService.readFile(filePath)
# print(file.createdTime)
# print(file.lastModificationTime)

# ==renameFolder==
# path = r'D:\python\apps\manapic\img'
# folder = GlobalService.readPath(path)
# # print(folder.size)
# GlobalService.renameFolder(folder, "newImg")

# ==renameDuplicatedFolderNames==
path = r'D:\python\apps\manapic\img'
folder = GlobalService.readPath(path)
GlobalService.renameDuplicatedFolderNames(folder.listAllFoldersPaths, folder.listAllFoldersNames)

