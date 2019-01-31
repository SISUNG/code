"""
#进入小甲鱼的网站
import urllib.request

path = 'http://www.fishc.com'

res = urllib.request.urlopen(path)

html = res.read().decode('utf-8')

print(html)
"""

"""
#下载一只小猫
import urllib.request as ur
res = ur.urlopen('http://placekitten.com/g/200/300')
out = res.read()
f = open('cat.jpg', 'wb')
f.write(out)
f.close()
"""

import urllib.request
req = urllib.request.Request('http://www.fishc.com/ooxx.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read().decode('utf-8'))