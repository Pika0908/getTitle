import requests
from lxml import etree

import urllib
def url( word ):
    return urllib.parse.quote( word )

import base64
def b64( word ):
    b =base64.b64encode( word.encode('utf-8') ).decode( "utf-8" )
    return b

class Craw():
    def __init__(self, keyword ):
        self.keyword = keyword

    def getTitle( self, link ):
        res = requests.get( link )
        res.encoding = 'big5'
        pa = etree.HTML( res.text )
        tmp1 = pa.xpath( '//div[contains(@id, "con_")]/a' )
        for title in tmp1:
            print( "".join( title.itertext() ) )

keyword_in = input("keyword: ")
keyword_tmp = url( keyword_in )
keyword = b64 ( keyword_tmp )
link = "https://www.pcstore.com.tw/adm/psearch.htm?store_k_word=" + keyword + "&slt_k_option=1"

test_1 = Craw( keyword )
test_1.getTitle( link )
