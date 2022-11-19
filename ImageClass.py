import FileClass as F

class Image(F.File):
    def __init__(self, path):
        F.File.__init__(self, path)
        # #########写到这儿了
        self.DateTimeOriginal = ''