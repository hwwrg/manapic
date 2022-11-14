import os
import time
from datetime import datetime


class File:
    def __init__(self, path):
        """_summary_

        Args:
            path (String): _description_
        """        
        self.path = path
        self.name = path[path.rfind("\\"):][1:]
        self.size = os.path.getsize(path)
        self.createdTime = time.ctime(os.path.getctime(path))
        self.createdTime = datetime.strptime(
            self.createdTime, "%a %b %d %H:%M:%S %Y").strftime('%Y-%m-%d %H:%M:%S')
        self.lastModificationTime = time.ctime(os.path.getmtime(path))
        self.lastModificationTime = datetime.strptime(
            self.lastModificationTime, "%a %b %d %H:%M:%S %Y").strftime('%Y-%m-%d %H:%M:%S')
