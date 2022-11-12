
import GlobalService

# path = "./img"

# print('=======================================')
# pathInfo = PathService.explorPath(path)
# # print(pathInfo)
# print('=======================================')

# listFiles = PathService.getListFiles(path)
# print(listFiles)
# print('=======================================')

# listPaths = PathService.getListPaths(path)
# print(listPaths)
# print('=======================================')

# listFolderNames = PathService.getListFolderNames(path)
# print(listFolderNames)


path = input()
f = GlobalService.readPath(path)
print(f.path)