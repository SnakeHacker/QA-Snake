#coding:utf8

import urllib,urllib2
import re
from bs4 import BeautifulSoup

def get_html(url):
    pass
    headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
    # req = urllib2.Request(url="http://baike.baidu.com/item/王思聪",headers=headers)
    req = urllib2.Request(url=url,headers=headers)
    socket = urllib2.urlopen(req)
    content = socket.read()
    socket.close()
    soup = BeautifulSoup(content, "lxml")
    # print(soup.prettify())
    return soup

'''
print answer
'''
def ptranswer(ans,ifhtml):
    result = ''
    print ans
    for answer in ans:
        if ifhtml:
            print answer
        else:
            if answer == u'\n':
                # print '回车'
                continue
            p = re.compile('<[^>]+>')
            # print '##############'
            # print answer
            # print type(answer)
            # if answer.name == 'br':
            #     continue
            # print p.sub("", answer.string)
            # print '##############'
            result += p.sub("", answer.string).encode('utf8')
    return result


def ltptools(args):
    url_get_base = "http://api.ltp-cloud.com/analysis/"
    result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
    content = result.read().strip()
    return content


if __name__ == '__main__':
    pass
    args = {
        'api_key' : 'F1e194G841HHvTDhqb4JsGrHHw4Q0DYFbzKqgQNm',
        'text' : '太阳为什么是圆的。',
        'pattern' : 'srl',
        'format' : 'json'
    }
    content = ltptools(args=args)
    print content