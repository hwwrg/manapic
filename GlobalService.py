import os
import time
import Folder as FD


def readPath(path): 
    
    if os.path.exists(path) == False:
        return "The path entered does not exist. Please retry."
    
    folder = FD.Folder(path)   
    
    """_summary_

            folder.path = path
            folder.name = ''
            folder.size = 0
            folder.createdTime = ''
            folder.lastModificationTime = ''
            folder.listAllFiles = []
            folder.listRootFiles = []
            folder.listAllPaths = []
            folder.listRootPaths = []
            folder.listAllFolders = []
            folder.listRootFolders = []
    """


    
    return folder


