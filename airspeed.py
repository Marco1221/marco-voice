# -*- coding: utf-8 -*-
import pygame,sys,pyaudio,wave,urllib,urllib2,sys,json,random,string
from pydub import AudioSegment
from aip import AipSpeech
APP_ID = '10282742' # 百度应用的 APP_ID
API_KEY = 'AO19LSgzfj7rQDW8vHOkZhGV' # 百度应用的 API_KEY
SECRET_KEY = 'ebff9e67d56500c7972aa50a10012d9e' # 百度应用的 SECRET_KEY
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
reload(sys)
sys.setdefaultencoding('utf-8')

API_KEY = 'aad1816a5abc4930bc78f6ed8aa2ccf7'   # 这里是获取的图灵APIkey
raw_TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY

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
            return '主人:' +content+hjson['url']
        elif length==2:
            return '主人:' +content

if __name__=='__main__':
    varst=1
    while varst == 1 :
        print ("".decode('utf-8'))
        strInput = result()
        print (strInput)

#        print (contents)
#while 1 == 1:
#    print('请输入要转换成为语音的文字：')
#    strInput = raw_input()
        resultvoice  = aipSpeech.synthesis(strInput, 'zh', 1, {
            'vol': 5,
        })
        if not isinstance(result, dict): #百度提供的方法
            mp3salt = ''.join(random.sample(string.ascii_letters + string.digits, 8)) # 生成随机8位字符串的文件名
            with open(mp3salt + '.mp3', 'wb') as f:  # 转换的mp3 写入文件
                f.write(resultvoice)
                f.close()
                print('转换成功！开始播放')
                pygame.mixer.init(frequency=15500,size=-16,channels=4) # 设置播放效果
                pygame.mixer.music.load(mp3salt + '.mp3')
                pygame.mixer.music.play() # 循环0次 从第0秒开始播放
#mp3file = AudioSegment.from_mp3("/root/voice/" + mp3salt + '.mp3')
#mp3file.export("/root/voice/" + mp3salt + '.wav', format="wav")
#def get_file_content(filePath):
#    with open(mp3salt + '.wav', 'rb') as fp:
#        return fp.read()
# 识别本地文件
#aipSpeech.asr(get_file_content(mp3salt + '.wav'), 'wav', 16000, {
#    'lan': 'zh',
#})