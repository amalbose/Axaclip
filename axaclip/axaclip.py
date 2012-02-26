'''
Created on Feb 20, 2012

@author: axatrikx
'''

import time
'''
Axaclip class 
'''
class Axaclip:
    
    '''
    @param name: the name of the code snippet
    '''
    def __init__(self,name):
        self.name=name
        self.__id=self.generate_ID()
        
    '''
    sets the values for the axaclip class
    @param lang: the programming language
    @param url: the url for the snippet  
    @param description: a description for what the code does
    @param contents: the code contents
    @param keywords: a list of keyword strings 
    '''
    def setValues(self,lang,url,description,contents,*keywords):
        self.__lang=lang
        self.__url=url
        self.__description=description
        self.__contents=contents
        self.__keywords=keywords
        self.__dateCreated=time.asctime( time.localtime(time.time()) )
    
    def generate_ID(self):
        return 1
    

    
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id


    def get_lang(self):
        return self.__lang


    def get_url(self):
        return self.__url


    def get_description(self):
        return self.__description


    def get_contents(self):
        return self.__contents


    def get_keywords(self):
        return self.__keywords


    def get_date_created(self):
        return self.__dateCreated


    def set_name(self, value):
        self.__name = value


    def set_lang(self, value):
        self.__lang = value


    def set_url(self, value):
        self.__url = value


    def set_description(self, value):
        self.__description = value


    def set_contents(self, value):
        self.__contents = value


    def set_keywords(self, value):
        self.__keywords = value


    def set_date_created(self, value):
        self.__dateCreated = value


   

