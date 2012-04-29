from axaclip.CodeSnip import CodeSnip
from axaclip.AxaFileMan.FileActions import createFile
from axaclip.Indexer.Indexer import addToIndex

def addSnippet(name,language,description,content,url,*keywords):
    codeSnipObj = CodeSnip(name,language,description,content,url,keywords)
    fileResult = codeSnipObj.toFileString()
    fileCreateResult = createFile(codeSnipObj.get_name(), fileResult)

    if fileCreateResult:
    	addToIndex("")