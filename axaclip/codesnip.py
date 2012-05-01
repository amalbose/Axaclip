'''
Created on Feb 20, 2012

@author: axatrikx
'''
import time

KEYBOARD_SEPERATOR=", "

class CodeSnip:

    def __init__(self, name):
        "Initializes CodeSnip by setting name and setting others to empty string"
        self.__name = name
        self.__lang = self.__url = self.__description = \
            self.__contents = self.__keywords = self.__dateCreated = ""
        
        
    def setValues(self, lang, url, description, contents, keywords=(("",""),)):
        "Sets the values as provided"
        self.__lang = lang
        self.__url = url
        self.__description = description
        self.__contents = contents
        self.__keywords = KEYBOARD_SEPERATOR.join(keywords)
        self.__dateCreated = time.asctime( time.localtime(time.time()) )
        
    def get_name(self):
        "Returns the name"
        return self.__name

    def get_lang(self):
        "Returns the language"
        return self.__lang


    def get_url(self):
        "Returns the URL"
        return self.__url


    def get_description(self):
        "Returns the description"
        return self.__description


    def get_contents(self):
        "Returns the code contents"
        return self.__contents


    def get_keywords(self):
        "Returns the keywords"
        return self.__keywords


    def get_date_created(self):
        "Returns the date created"
        return self.__dateCreated


    def set_name(self, value):
        "Sets the name"
        self.__name = value


    def set_lang(self, value):
        "Sets the language"
        self.__lang = value


    def set_url(self, value):
        "Sets the URL"
        self.__url = value


    def set_description(self, value):
        "Sets the description"
        self.__description = value

    def set_contents(self, value):
        "Sets the code contents"
        self.__contents = value


    def set_keywords(self, value):
        "Sets the keywords"
        self.__keywords = value


    def set_date_created(self, value):
        "Sets the created date"
        self.__dateCreated = value
    
    def toFileString(self):
        "Formats the various items in writable format"
        return "\n".join(["Name:\t" + self.get_name(), 
                          "Language:\t" + self.get_lang(),
                          "Description:\t" + self.get_description(),
                          "Contents:\t" + self.get_contents(), 
                          "Keywords:\t" + self.get_keywords(),
                          "URL:\t" + self.get_url(),
                          "Date:" + self.get_date_created()])
