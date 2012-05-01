'''
Created on Apr 28, 2012

@author: amalbose

Perform file actions like creating new file, reading, 
editing and deleting existing files.

'''
from os import remove
from os.path import exists
from distutils.dir_util import mkpath

def createFile(fileName,fileContent):
    "Creates file with the given contents"
    _prepareDirectory(fileName)
    try:
        fileHandle = open(fileName,"w")
        try:
            fileHandle.write(fileContent)
        finally:
            fileHandle.close()
    except IOError:
        return False
    return True
    
def editFile(fileName,fileContent):
    "Replaces the contents of the file with the given contents"
    try:
        fileHandle = open(fileName, "a")
        try:
            fileHandle.write(fileContent)
        finally:
            fileHandle.close()
    except IOError:
        return False
    return True
    
def readFile(fileName):
    "Reads and returns the contents as String"
    try:
        fileHandle = open(fileName, "r")
        try:
            contents = fileHandle.readlines()
        finally:
            fileHandle.close()
    except IOError:
        return False
    return contents
    
def removeFile(fileName):
    "Deletes the file"
    remove(fileName)
    

def _prepareDirectory(fileName):
    "Creates directory if not present"
    #removes the file rename and retains the folder path
    directory = "/".join(fileName.split("/")[:-1])
    if not exists(directory):
        mkpath(directory)
