try:
    import urllib.request
    req = urllib.request.urlopen('http://www.baidu.com')
    print(req.read())
except FloatingPointError:
    print('Capture FloatingPointError')
except IOError:
    print('Capture IOError')
except Exception:
    print('Capture Error')
except:
    print('Capture Error')
