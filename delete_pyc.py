import os, glob


def scandirs(path):
    for currentFile in glob.glob( os.path.join(path, '*') ):
        if os.path.isdir(currentFile):
            print ('got a directory: ' + currentFile)
            scandirs(currentFile)
        print ("processing file: " + currentFile)

        if currentFile.endswith('pyc'):
            os.remove(currentFile)

scandirs('./')