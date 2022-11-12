class Folder:

    def __init__(self, path):  
            self.path = path
            self.name = ''
            self.size = 0
            self.createdTime = ''
            self.lastModificationTime = ''
            self.listAllFiles = []
            self.listRootFiles = []
            self.listAllPaths = []
            self.listRootPaths = []
            self.listAllFolders = []
            self.listRootFolders = []

    def explorFolder(self):    
        pass
 
    def rename(self, newName):
        """_summary_

        Args:
            newName (_type_): _description_
        """        
        self.name = newName
         
