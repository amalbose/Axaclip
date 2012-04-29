'''
Created on Apr 28, 2012

@author: amalbose

Perform file actions like creating new file, reading, 
editing and deleting existing files.

'''

import os
from distutils.dir_util import *

def createFile(fileName,fileContent):
    "Creates file with the given contents"
    prepareDirectory(fileName)
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
    os.remove(fileName)
    

def prepareDirectory(fileName):
    "Creates directory if not present"
    directory = "/".join(fileName.split("/")[:-1])
    if not os.path.exists(directory):
        mkpath(directory)
