from PIL import Image
from PIL.ExifTags import TAGS
import subprocess
import json
import piexif
import os

import FileClass as FC
import GlobalService as GS


def getExifTags(imgPath):
    """create an <Image> object of file information and ExifTags.
        -ExifTags
        GPSInfo
        ResolutionUnit
        ExifOffset
        Make
        Model
        Software
        Orientation
        DateTime
        YCbCrPositioning
        XResolution
        YResolution
        ExifVersion
        ComponentsConfiguration
        FlashPixVersion
        DateTimeOriginal
        DateTimeDigitized
        ExposureBiasValue
        ColorSpace
        MeteringMode
        LightSource
        Flash
        FocalLength
        ExifImageWidth
        ExifImageHeight
        ExifInteroperabilityOffset
        SceneCaptureType
        SubjectDistanceRange
        OffsetTime
        OffsetTimeOriginal
        OffsetTimeDigitized
        SubsecTime
        SubsecTimeOriginal
        SubsecTimeDigitized
        ExposureTime
        FNumber
        CustomRendered
        ISOSpeedRatings
        ExposureMode
        WhiteBalance
        DigitalZoomRatio
        MakerNote

    Args:
        imgPath (str): _description_
    """
    image = Image.open(imgPath)
    info = image._getexif()
    tags = {}
    for k, v in info.items():
        nice = TAGS.get(k)
        tags[nice] = v
    tags.popitem()  # 删除最后一项
    return tags


def renamePhotoNames(path):
    root = path
    photoNames = GS.readPath(root).listRootFiles
    newPhotoNames = []

    # get year, month, day
    for p in photoNames:
        # pName = p
        imgPath = GS.generateFilePath(root, p)
        try:
            tags = getExifTags(imgPath)
            createdTime = tags['DateTimeOriginal']
        except:
            createdTime = FC.File(imgPath).createdTime
        year, month, day = createdTime[0:4], createdTime[5:7], createdTime[8:10]
        newPhotoNames.append(f'{year}-{month}-{day}')

    # find duplicated names
    nameCountDict = {}
    index = 0
    for n in newPhotoNames:
        if n not in nameCountDict:
            nameCountDict[n] = 0
        else:
            nameCountDict[n] += 1
            newPhotoNames[index] = n.replace('.', f'({nameCountDict[n]}).')
        index += 1

        # rename files
    for i in range(len(photoNames)):
        p = photoNames[i]
        pFomat = p[p.rfind('.') + 1:]
        GS.rename(f'{root}\{photoNames[i]}', newPhotoNames[i] + pFomat)


def get_video_info(video_file):
    cmd = ['ffprobe', '-v', 'quiet', '-print_format',
           'json', '-show_format', '-show_streams', video_file]
    result = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    data = json.loads(result)
    return data


def get_video_creation_time(video_file):
    data = get_video_info(video_file)
    try:
      return data['streams'][0]['tags']['creation_time'][:10]
    except:
        createdTime = FC.File(video_file).createdTime
        year, month, day = createdTime[0:4], createdTime[5:7], createdTime[8:10]
        return f'{year}-{month}-{day}'
    

def rotate_image_with_exif_fix(img_path):
    with Image.open(img_path) as img:
        # Rotate image according to EXIF orientation tag
        exif_dict = piexif.load(img.info["exif"])
        orientation = exif_dict.get("0th", {}).get(piexif.ImageIFD.Orientation)
        if orientation == 2:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 3:
            img = img.rotate(180)
        elif orientation == 4:
            img = img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 5:
            img = img.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 6:
            img = img.rotate(-90, expand=True)
        elif orientation == 7:
            img = img.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 8:
            img = img.rotate(90, expand=True)
        else:
            pass

        # Save rotated image with original exif information
        exif_bytes = piexif.dump(exif_dict)
        img.save(img_path, "jpeg", exif=exif_bytes)


