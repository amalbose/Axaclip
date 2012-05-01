from axaclip.codesnip import CodeSnip
from axaclip.axafiler.fileactions import createFile


class Controller:

    def __init__(self,directoryPath):
        "Sets the base folder for Axaclip"
        self.FOLDERNAME = directoryPath

    def addSnippet(self,name,language,description,content,url,keywords=(("",""),)):
        "Adds a new snippet with the given contents"
        
        result = self._getsStringToWrite(name,language,description,content,url,keywords)
        if result:
            print "DONE"
        else:
            print "ERROR"
            
            
    def _getsStringToWrite(self,name,language,description,content,url,keywords=(("",""),)):
        "Creates the string to write to file from given details"
        #creates CodeSnip object and sets the values
        codeSnipObj = CodeSnip(name)
        codeSnipObj.setValues(language,url,description,content,keywords)
        
        #gets the string to write to file
        fileResult = codeSnipObj.toFileString()
        #writes to file
        fileCreateResult = createFile(self.FOLDERNAME +codeSnipObj.get_lang().capitalize()+"/"+ codeSnipObj.get_name(), fileResult)
        return fileCreateResult