'''
Created on Apr 28, 2012

@author: amalbose

Perform file actions like creating new file, reading, 
editing and deleting existing files.

'''

import os,sys

def createFile(fileName,fileContent):
    prepareDirectory(fileName)
    try:
        fileHandle = open(fileName,"w")
        try:
            fileHandle.write(fileContent)
        finally:
            fileHandle.close()
    except IOError,e:
        print e
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
    

def prepareDirectory(fileName):
    directory = fileName.split("/")[0]
    if not os.path.exists(directory):
        print directory
        os.mkdir(directory)