# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json
import base64
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--imagePath", action="store", type="string", dest="imagePath", default="./test.jpg", help="input image path")
(options, args) = parser.parse_args()

imagePath = options.imagePath
print "imagePath:"+imagePath
f=open(imagePath,'rb') #二进制方式打开图文件 
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
#print(ls_f)

url = 'http://apis.baidu.com/apistore/idlocr/ocr'

data = {}
data['fromdevice'] = "pc"
data['clientip'] = "10.10.10.0"
data['detecttype'] = "LocateRecognize"
data['languagetype'] = "CHN_ENG"
data['imagetype'] = "1"
data['image'] = ls_f
decoded_data = urllib.urlencode(data)
req = urllib2.Request(url, data = decoded_data)

req.add_header("Content-Type", "application/x-www-form-urlencoded")
req.add_header("apikey", "e952b9cf7e398fd2ee3a258ecd3a6ea2")

resp = urllib2.urlopen(req)
content = resp.read()

if(content):
    #print(str(content).replace("\\u", "\u"))
    con = json.loads(content)
    print "con",(type(con))
    retD = con['retData']
    print "retdata:",len(retD)
    for i in retD:
        print "left:"+i['rect']['left'],"top:"+i['rect']['top'],"width:"+i['rect']['width'],"height:"+i['rect']['height'],"word:"+i['word']
    
