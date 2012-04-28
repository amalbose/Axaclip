from axaclip import CodeSnip


def addSnippet(name,language,description,content,url,*keywords):
	''' Creates new CodeSnip object and 
		Creates new File in default location
	'''
	codeSnipObj = CodeSnip.CodeSnip(name,language,description,content,url,keywords)
	