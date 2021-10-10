# Written by Patrick Keener on 10/28/2020
# Video Link: https://youtu.be/TRNcntVyJ3I
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
#
# DSC 430: Python Programming
# Assignment 0602: Surf CDM

# What are the 25 most common words on the CDM website?

from html.parser import HTMLParser
from urllib.request import urlopen


class linkParser(str):
    """ This class is to be used to parse the URLs from the .html file. """

    def __init__(self, link = 'www.cdm.com'):
        """ init link """
        self.value = str(link)
        self.scheme = str()
        self.host = str()
        self.pathName = str()
        self.isLink = False
        self.updateLink(self.value)

    def updateLink(self, link):
        """ Update the link- allows for a single mutable object to handle all links"""

        fileTypes = ['.aspx', '.html']

        self.value = str(link)

        if self.value[:4] == 'http':
            # update entire link
            self.scheme = self.updateScheme(self.value)
            self.host = self.updateHost(self.value)
            self.pathName = self.updatePathName(self.value)
            self.isLink = True

        elif self.value[-5:] in fileTypes:
            # update relative path
            self.pathName = self.updateRelativePathName(self.value)
            self.isLink = True

        else:
            self.isLink = False
            return 

    def updateScheme(self, link):
        """ Update the schema """

        schemeEnd = link.find('/')
        self.scheme = str(link[:schemeEnd])
        return self.scheme
    
    def updateHost(self, link):
        """ Update the schema """

        schemeEnd = link.find('/')

        # This makes the code somewhat less generalizable since manually need to
        # specify the type of web page
        if self.value.find('.com') == -1: 
            return
        else:
            hostEnd = self.value.find('.com') + 4

        self.host = str(link[schemeEnd:hostEnd])
        return self.host
    
    def updatePathName(self, link):
        """ updates the path"""

        # This makes the code somewhat less generalizable since manually need to
        # specify the type of web page
        if self.value.find('.com') == -1: 
            return
        else:
            hostEnd = self.value.find('.com') + 4

        self.pathName = self.value[hostEnd:]
        return self.pathName
    
    def updateRelativePathName(self, link):
        """ updates the path"""
        self.pathName = self.value
        return self.pathName
    
    def getPathName(self):
        """ Returns path """
        return str(self.pathName)

        
class ParserExtended(HTMLParser):
    """ used to parse HTML, customized for this project"""
    
    def __init__(self, *, convert_charrefs=True):
        """ Initialize and reset this instance.
        If convert_charrefs is True (the default), all character references
        are automatically converted to the corresponding Unicode characters.
        """
        self.convert_charrefs = convert_charrefs
        self.reset()
        self.wordCount = dict()
        self.linkList = list()
        self.link = linkParser()
    
    def handle_starttag(self, tag, attrs):
        'print value of href attribute if any'
        if tag == 'a':
            # search for href attribute and print its value
            for attr in attrs:
                if attr[0] == 'href':
                    self.link.updateLink(attr[1])
                    if self.link.isLink:
                        if 'cdm.depaul.edu' in self.link.host:
                            self.linkList.append(self.link.getPathName())
                    print(attr[1])

                    # parse link- class?

    def handle_data(self, data):
        """  Count words and adds to dictionary
        """
        targetString = str(data).split(sep = ' ')
    
        for word in targetString: # If key doesn't exist, create it & iterate
            self.wordCount[word] = self.wordCount.get(word, 0) + 1 


def crawl(spider):
    """ crawls the link list to check each page for words """
    for link in spider.linkList:
        response = urlopen('link')
        html = response.read()
        response.close()
        spider.feed(html.decode())
    return None


def wordCounter():
    """ This program crawls the CDM website and determines what the 25 most 
    common words are.
    """
    spider = ParserExtended()
    crawl(spider)

    return None

wordCounter()


def linkParserTest():
    """
    Testing the link parser
    """
    linkTest = linkParser('http://www.google.com/test/anotherTest.aspx')
    print(str(linkTest.scheme))
    print(str(linkTest.host))
    print(str(linkTest.pathName))

    linkTest.updateLink('https://www.google.com/test2/aFourthTest/')
    print(str(linkTest.scheme))
    print(str(linkTest.host))
    print(str(linkTest.pathName))

    linkTest.updateLink('/test/anotherTest.aspx')
    print(str(linkTest.scheme))
    print(str(linkTest.host))
    print(str(linkTest.pathName))

    linkTest.updateLink('https://securelb.imodules.com/s/1906/19/interior.aspx?sid=1906&gid=2&pgid=853&cid=2668')
    print(str(linkTest.scheme))
    print(str(linkTest.host))
    print(str(linkTest.pathName))
    
    return None

linkParserTest()