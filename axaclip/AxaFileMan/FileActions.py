'''
Created on Apr 28, 2012

@author: amalbose

Perform file actions like creating new file, reading, 
editing and deleting existing files.

'''

import os

def createFile(fileName,fileContent):
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
    fileHandle = open(fileName,"a")
    fileHandle.write(fileContent)
    fileHandle.close()
    
def readFile(fileName):
    fileHandle = open(fileName,"r")
    return fileHandle.readlines()
    
def removeFile(fileName):
    os.remove(fileName)