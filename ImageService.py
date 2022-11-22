from PIL import Image
from PIL.ExifTags import TAGS

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

