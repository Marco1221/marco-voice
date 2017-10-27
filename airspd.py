# -*- coding: utf-8 -*-
import pygame,sys,urllib,urllib2,sys,json,random,string
from aip import AipSpeech
APP_ID = '10282742' # 百度应用的 APP_ID
API_KEY = 'AO19LSgzfj7rQDW8vHOkZhGV' # 百度应用的 API_KEY
SECRET_KEY = 'ebff9e67d56500c7972aa50a10012d9e' # 百度应用的 SECRET_KEY
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
reload(sys)
sys.setdefaultencoding('utf-8')

TU_API_KEY = 'aad1816a5abc4930bc78f6ed8aa2ccf7'   # 这里是获取的图灵APIkey
raw_TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % TU_API_KEY

def result():
    for i in range(1,100):
        queryStr = raw_input("我:".decode('utf-8'))
        TULINURL = "%s%s" % (raw_TULINURL,urllib2.quote(queryStr))
        req = urllib2.Request(url=TULINURL)
        result = urllib2.urlopen(req).read()
        hjson=json.loads(result)
        length=len(hjson.keys())
        content=hjson['text']

        if length==3:
            return ':' +content+hjson['url']
        elif length==2:
            return ':' +content

if __name__=='__main__':
    varst=1
    while varst == 1 :
        print ("".decode('utf-8'))
        strInput = result()
        print (strInput)
        resultvoice  = aipSpeech.synthesis(strInput, 'zh', 1, {
            'vol': 5,
        })
        if not isinstance(result, dict): #百度提供的方法
            mp3salt = ''.join(random.sample(string.ascii_letters + string.digits, 8)) # 生成随机8位字符串的文件名
            with open(mp3salt + '.mp3', 'wb') as f:  # 转换的mp3 写入文件
                f.write(resultvoice)
                f.close()
                pygame.mixer.init(frequency=15500,size=-16,channels=4) # 设置播放效果
                pygame.mixer.music.load(mp3salt + '.mp3')
                pygame.mixer.music.play() # 循环0次 从第0秒开始播放