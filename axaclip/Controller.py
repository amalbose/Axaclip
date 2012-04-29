from axaclip.CodeSnip import CodeSnip
from axaclip.AxaFileMan.FileActions import createFile
from axaclip.Indexer.Indexer import addToIndex

FOLDERNAME = "Snippets/"

def addSnippet(name,language,description,content,url,keywords):
    codeSnipObj = CodeSnip(name)
    codeSnipObj.setValues(language,url,description,content,keywords)
    fileResult = codeSnipObj.toFileString()
    fileCreateResult = createFile(FOLDERNAME+codeSnipObj.get_name(), fileResult)

    if fileCreateResult:
    	addToIndex("")