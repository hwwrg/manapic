import FileClass as FC

class Image(FC.File):
    """ExifTags as attributes
    use Image.__dict__() to get all attributes in a dictionnary

    Args:
        F (File): _description_
    """    
    def __init__(self, path):
        FC.File.__init__(self, path)
        self.GPSInfo = ''
        self.Make = ''
        self.Model = ''
        self.Orientation = ''
        self.DateTime = ''
        self.DateTimeOriginal = ''
        self.DateTimeDigitized = ''
        self.ExposureBiasValue = ''
        self.ColorSpace = ''
        self.MeteringMode = ''
        self.LightSource = ''
        self.Flash = ''
        self.FocalLength = ''
        self.ExifImageWidth = ''
        self.ExifImageHeight = ''
        self.ExifInteroperabilityOffset = ''
        self.OffsetTime = ''
        self.OffsetTimeOriginal = ''
        self.OffsetTimeDigitized = ''
        self.SubsecTime = ''
        self.SubsecTimeOriginal = ''
        self.SubsecTimeDigitized = ''
        self.ExposureTime = ''
        self.FNumber = ''
        self.CustomRendered = ''
        self.ISOSpeedRatings = ''
        self.ExposureMode = ''
        self.WhiteBalance = ''
        self.DigitalZoomRatio = ''
        
import GlobalService as GS

root = r"D:\python\apps\manapic\imgForImgService"
imgName = r"20220820_232743.JPG"
imgPath = GS.generateFilePath(root, imgName)
test = Image(imgPath)
print(test.__dict__)
