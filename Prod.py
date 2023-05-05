from tkinter.font import names
import GlobalService
import ImageService
import FileClass
import os

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

# ==get_video_creation_time==
# print(ImageService.get_video_creattion_time(vid_path))


# import ffmpeg
#
# metadata = ffmpeg.probe('MAH05648.MP4')
# print(metadata)

# ==rename by creationg date==
root = r'D:\test'
ImageService.renamePhotoNames(root)

# ==process_folder==
# def process_folder(folder_path):
#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
#         if os.path.isfile(file_path) and file_name.endswith(".jpg"):
#             ImageService.rotate_image_with_exif_fix(file_path)

# folder_path = r"D:\照片备份\2012-2月 回老家"
# process_folder(folder_path)

# img_path = r"D:\照片备份\2012-2月 回老家\IMG_5721.JPG"
# ImageService.rotate_image_with_exif_fix(img_path)



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

# ==rename by given new name==
# path = r'D:\python\apps\manapic\newImg'
# path = r'D:\test'
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
# path = r'D:\photo_album'
# GlobalService.createFoldersByDay(path)

# ==remove_files_to_folder_by_creation_day==
# path = r'D:\rx100'
# GlobalService.remove_files_to_folder_by_creation_day(path)



