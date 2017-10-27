# -*- coding: utf-8 -*-
from aip import AipSpeech
APP_ID = '10282742' # 百度应用的 APP_ID
API_KEY = 'AO19LSgzfj7rQDW8vHOkZhGV' # 百度应用的 API_KEY
SECRET_KEY = 'ebff9e67d56500c7972aa50a10012d9e' # 百度应用的 SECRET_KEY
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
# 识别本地文件
aipSpeech.asr(get_file_content('audio.pcm'), 'pcm', 16000, {
    'lan': 'zh',
})
# 从URL获取文件识别
#aipSpeech.asr('', 'pcm', 16000, {
#    'url': 'http://121.40.195.233/res/16k_test.pcm',
#    'callback': 'http://xxx.com/receive',
#})