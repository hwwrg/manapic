from tkinter.font import names
import GlobalService
import ImageService
import FileClass

import json
import shutil



# path = input()

# @@@@@@ ImageService @@@@@@
# root = r'D:\rx100'
# vid_name = 'MAH05649.MP4'
# vid_path = GlobalService.generateFilePath(root, vid_name)
# ==getExifTags==
# imgName = r"DSC08551.JPG"
# imgPath = GlobalService.generateFilePath(root, imgName)
# test = ImageService.getExifTags(imgPath)
# print(test)

# ==get_video_info(video_file)==
# info = ImageService.get_video_info(vid_path)
# formatted_data = json.dumps(info, indent=4)
# print(formatted_data, type(formatted_data))
# print(info['streams'][0]['tags']['creation_time'])

# ==get_video_creattion_time==
# print(ImageService.get_video_creattion_time(vid_path))


# import ffmpeg
#
# metadata = ffmpeg.probe('MAH05648.MP4')
# print(metadata)

# ==renamePhoto==
# root = r'D:\照片编辑\2023相册\00'
# ImageService.renamePhotoNames(root)


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

# ==is_video==
# root = r'D:\rx100'
# vid_name = 'MAH05649.MP4'
# vid_path = GlobalService.generateFilePath(root, vid_name)
# rs = GlobalService.is_video(vid_path)
# print(rs)

# ==createFoldersByMonth==
# path = r'D:\python\apps\manapic\imgOneFolder'
# listNewFolderNames = GlobalService.creatFoldersByMonth(path)
# print(listNewFolderNames)

# ==createFoldersByDay==
# path = r'D:\rx100'
# GlobalService.createFoldersByDay(path)

# ==remove_files_to_folder_by_creation_day==
# root = r'D:\rx100'
# GlobalService.remove_files_to_folder_by_creation_day(root)




