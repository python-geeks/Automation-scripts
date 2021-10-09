import os
import re
import win32api
import sys


class AlFileSearcher():

    def __init__(self, fileName):
        super().__init__()
        self.findFileInAllDrives(fileName)

    def findFile(self, rootFolder, rex):
        for root, dirs, files in os.walk(rootFolder):
            for f in files:
                result = rex.search(f)
                if result:
                    print(os.path.join(root, f))

    def findFileInAllDrives(self, fileName):
        rex = re.compile(fileName)
        for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
            self.findFile(drive, rex)


if __name__ == '__main__':
    AlFileSearcher(sys.argv[1])
