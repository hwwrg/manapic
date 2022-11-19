from PIL import Image
from PIL.ExifTags import TAGS

import GlobalService as GS


def readImg(imgPath):
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
    img = Image.open(imgPath)
    info = img._getexif()
    tags = {}
    for k, v in info.items():
        nice = TAGS.get(k)
        ########### 写到这儿了
        print(f'self.{nice} = {v}')
        # print(nice, v)
        # print('%s (%s) = %s' % (nice, k, v))

root = r"D:\python\apps\manapic\imgForImgService"
imgName = r"20220820_232743.JPG"
imgPath = GS.generatePath(root, imgName)
test = readImg(imgPath)