#encoding=utf-8

import sys
import urllib
import urllib2
data1 = urllib.quote(raw_input().decode(sys.stdin.encoding).encode('utf8'))
print (data1)
url = "http://tsn.baidu.com/text2audio?tex=" + data1 + "&lan=zh&cuid=aip-cxy&ctp=1&tok=24.63af8851fa919b35e9b0db58e8644c60.2592000.1511595471.282335-10282742"
req = urllib2.Request(url)
#print req

res_data = urllib2.urlopen(req)
res = res_data.read()
#print res
