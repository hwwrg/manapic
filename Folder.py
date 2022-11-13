class Folder:
    """_summary_
    """
    def __init__(self, path):
        self.path = path
        self.name = ''
        self.size = 0
        self.createdTime = ''
        self.lastModificationTime = ''

        # files and folders in root
        self.listRootFiles = []
        self.listRootFoldersPaths = []
        self.listRootFoldersNames = []

        # files and folders in all levels
        self.listAllFiles = []
        self.listAllFoldersPaths = []
        self.listAllFoldersNames = []

    def explorFolder(self):
        pass

    def rename(self, newName):
        self.name = newName