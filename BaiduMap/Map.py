#coding:utf8

import urllib2
import json

mode = 'transit'
origin = '清华大学'
destination = '天安门'
origin_region  = ''
destination_region = ''
output = ''


url = "http://api.map.baidu.com/direction/v1?mode="+mode\
      +"&origin="+origin\
      +"&destination="+destination\
      +"&origin_region="+origin_region\
      +"&destination_region="+destination_region\
      +"&output="+output\
      +"&ak=GuGZ01jekpjxCa1IGQCDNv608jm48wDt"

req = urllib2.Request(url)
res = urllib2.urlopen(req)

print res.read()
