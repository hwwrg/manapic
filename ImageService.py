from PIL import Image
from PIL.ExifTags import TAGS

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
    tags.popitem()
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
        newPhotoNames.append(f'{month}-{year}-{day}.')

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
