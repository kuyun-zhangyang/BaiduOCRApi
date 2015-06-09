# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json
import base64
import os
import shutil
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--imagePath", action="store", type="string", dest="imagePath", default="./data", help="input image path")
(options, args) = parser.parse_args()

imagePath = options.imagePath

if os.path.isdir(imagePath):  # 判断是否存在路径
        print ("Directory is exit")
else:
        print ("Directory is not exit,please input right dir...."+txtFilePath) 
        time.sleep(5)     #程序休眠5秒
        exit()            #程序自动退出
url = 'http://apis.baidu.com/apistore/idlocr/ocr'

data = {}
data['fromdevice'] = "pc"
data['clientip'] = "10.10.10.0"
data['detecttype'] = "LocateRecognize"
data['languagetype'] = "CHN_ENG"
data['imagetype'] = "1"

filelist = []
filelist = os.listdir(imagePath) #得到文件名
for i in filelist:
		if i[len(i)-3:] == "jpg":
			imgPath = imagePath+'/'+i
			print "imagePath:"+imgPath
			f=open(imgPath,'rb') #二进制方式打开图文件 
			ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
			f.close()
			data['image'] = ls_f
			decoded_data = urllib.urlencode(data)
			req = urllib2.Request(url, data = decoded_data)
			req.add_header("Content-Type", "application/x-www-form-urlencoded")
			req.add_header("apikey", "e952b9cf7e398fd2ee3a258ecd3a6ea2")
			resp = urllib2.urlopen(req)
			content = resp.read()
			if(content):
				con = json.loads(content)
				#print "con",(type(con))
				fw = open(imgPath+".txt","w")
				retD = con['retData'] 
				print "retdata:",len(retD)
				for i in retD:
					print "left:"+i['rect']['left'],"top:"+i['rect']['top'],"width:"+i['rect']['width'],"height:"+i['rect']['height'],"word:"+i['word']
					fw.write(("left:"+i['rect']['left']).encode('utf-8'))
					fw.write(("top:"+i['rect']['top']).encode('utf-8'))
					fw.write(("width:"+i['rect']['width']).encode('utf-8'))
					fw.write(("height:"+i['rect']['height']).encode('utf-8'))
					fw.write(("word:"+i['word']).encode('utf-8'))
					fw.write('\n')
				fw.close()	