
import urllib.request

req = urllib.request.urlopen('http://www.baidu.com')

print(req.read())