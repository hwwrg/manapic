import os
import time
from datetime import datetime
# import imghdr
from PIL import Image
import subprocess
import sys
from tqdm import tqdm


import FolderClass as FD
import FileClass as F
import ImageService as IS

# Progress bar function


def progress_bar(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    print('[%s] %s%s ...%s\r' %
          (bar, percents, '%', status), end='', flush=True)

# generate the location of a file
def generateFilePath(root, name):
    return os.path.join(root, name)


def readPath(path):
    """_summary_

    Args:
        path (String): _description_

    Returns:
        Folder.Folder : _description_
    """
    if os.path.exists(path) == False:
        print("The path entered does not exist. Please retry.")
        return

    # folder.path
    folder = FD.Folder(path)

    # folder.name
    folder.name = path[path.rfind("\\"):][1:]

    # folder.createdTime
    folder.createdTime = time.ctime(os.path.getctime(path))
    folder.createdTime = datetime.strptime(
        folder.createdTime, "%a %b %d %H:%M:%S %Y").strftime('%Y-%m-%d %H:%M:%S')

    # folder.lastModificationTime
    folder.lastModificationTime = time.ctime(os.path.getmtime(path))
    folder.lastModificationTime = datetime.strptime(
        folder.lastModificationTime, "%a %b %d %H:%M:%S %Y").strftime('%Y-%m-%d %H:%M:%S')

    # folder.listRootFiles = []
    # folder.listRootFoldersPaths = []
    # folder.listRootFoldersNames = []
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            folder.listRootFiles.append(item)
        elif os.path.isdir(os.path.join(path, item)):
            folder.listRootFoldersPaths.append(os.path.join(path, item))
            folder.listRootFoldersNames.append(item)
        else:
            print("Item is neither file nor dir. That should not exist.")

    # folder.size
    # folder.listAllFiles = []
    # folder.listAllFoldersPaths = []
    # folder.listAllFoldersNames = []
    for root, dirs, files in os.walk(path):
        for name in files:
            folder.size += os.path.getsize(os.path.join(root, name))
            folder.listAllFiles.append(name)
        for name in dirs:
            folder.listAllFoldersPaths.append(os.path.join(root, name))
            folder.listAllFoldersNames.append(name)

    return folder


def readFile(filePath):
    """_summary_

    Args:
        filePath (String): _description_

    Returns:
        File.File: _description_
    """
    return F.File(filePath)


def rename(path, newName):
    try:
        root = path[:path.rfind("\\")+1]
        os.rename(path, f'{root}{newName}')
        return f'SUCCESS \n New name : {newName}'
    except:
        print('An exception occurred')
        return f'FAILURE \n An exception occurred'


def checkDuplicatedFolderNamesExist(path):
    folder = readPath(path)
    listFolderNames = folder.listAllFoldersNames
    if len(set(listFolderNames)) != len(listFolderNames):
        print(f"### Path : {path} \n Duplicated folder names EXIST.")
        return True
    else:
        print(f"### Path : {path} \n Duplicated folder names DO NOT EXIST.")
        return False


def renameDuplicatedFolderNames(path):
    # readPath
    folder = readPath(path)
    listFolderNames = folder.listAllFoldersNames
    listfolderpaths = folder.listAllFoldersPaths
    # list of tuple of name and path
    listNamePath = list(zip(listFolderNames, listfolderpaths))

    # count number of same folder names and rename duplicated folders
    folderCountDict = {}
    for i in range(len(listFolderNames)):
        name = listFolderNames[i]
        if name not in folderCountDict:
            folderCountDict[name] = 0
        else:
            folderCountDict[name] += 1
            test = rename(listfolderpaths[i],
                          f'{name}({folderCountDict[name]})')
            print(f'Renaming \'{listfolderpaths[i]}\' : {test}')


def is_image(filename):
    try:
        with Image.open(filename) as img:
            return True
    except:
        return False


# def is_video(filename):
#     try:
#         result = subprocess.check_output(['ffmpeg', '-i', filename], stderr=subprocess.STDOUT)
#         return b'Video:' in result
#     except subprocess.CalledProcessError as ex:
#         return False


def is_video(file_path):
    result = subprocess.Popen(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                              'stream=codec_type', '-of', 'csv=p=0', file_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, _ = result.communicate()
    codec_type = stdout.decode().strip()
    if codec_type == 'video':
        return True
    else:
        return False


def creatFoldersByMonth(path):
    """count creattion dates of photos in root path and create folders 
    with the format yyyy-mm

    Args:
        path (str): _description_
    """
    # get list of created months
    print('*** Creating folders by year and month')
    listYearMonth = []
    listRootFiles = readPath(path).listRootFiles

    for file in listRootFiles:
        filePath = generateFilePath(path, file)
        if is_image(filePath):     # imghdr.what() : read format
            dateTimeOriginal = IS.getExifTags(filePath)['DateTimeOriginal']
            yearMonth = dateTimeOriginal[:7].replace(':', '-')
            listYearMonth.append(yearMonth)
        else:
            print(f'{file} is not a image file.')
    listYearMonth = list(set(listYearMonth))

    # create folders
    for ele in listYearMonth:
        if os.path.exists(generateFilePath(path, ele)):
            print(f'{ele} exists already.')
        else:
            os.makedirs(generateFilePath(path, ele))
            print(f'New folder \'{ele}\' has been created.')


def createFoldersByDay(path):
    """count creattion dates of photos in root path and create folders 
    with the format yyyy-mm-dd

    Args:
        path (str): _description_
    """
    # get list of created months
    print('*** Creating folders by year-month-day')
    list_year_mont_day = []
    listRootFiles = readPath(path).listRootFiles

    # Create a progress bar for the loop
    with tqdm(total=len(listRootFiles), desc='*** Reading files', ascii=True) as pbar:
        for file in listRootFiles:
            filePath = generateFilePath(path, file)
            if is_image(filePath):     # imghdr.what() : read format
                dateTimeOriginal = IS.getExifTags(filePath)['DateTimeOriginal']
                year_month_day = dateTimeOriginal[:10].replace(':', '-')
                list_year_mont_day.append(year_month_day)
            elif is_video(filePath):
                list_year_mont_day.append(
                    IS.get_video_creattion_time(filePath))
            else:
                print(f'{file} is not a image or video file.')
            # Update the progress bar
            pbar.update(1)
            # time.sleep(0.1)  # Simulate some work
    list_year_mont_day = list(set(list_year_mont_day))

    # create folders
    for ele in list_year_mont_day:
        if os.path.exists(generateFilePath(path, ele)):
            print(f'{ele} exists already.')
        else:
            os.makedirs(generateFilePath(path, ele))
            print(f'New folder \'{ele}\' has been created.')
