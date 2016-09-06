'''
Created on Sep 6, 2016

@author: shawn.shaohua.wang
'''
from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    
    def __init__(self):
        print(11)
        super(MyHtmlParser, self).__init__()
    
    def handle_starttag(self, tag, attrs):
        print(tag)
        if tag == 'ul':
            print('list^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        pass
        
    def handle_data(self, data):
        pass

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass
        

if __name__ == '__main__':
    with open('test.htm', 'r', encoding='utf-8') as htmlFile:
        parser = MyHtmlParser()
        data = htmlFile.read()
        print(data)
        parser.feed(data)

    