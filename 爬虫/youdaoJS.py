# coding:utf-8
"""
爬虫 有道翻译
模拟网页请求实现翻译功能

"""
import requests
import time
import random
import json

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

# 破解参数


def getsalt():
    s = int(time.time() * 1000) + random.randint(0, 10)
    return str(s)


def getmd5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()
    return sign


def getSign(key, salt):
    sign = "fanyideskweb" + str(key) + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getmd5(sign)
    return sign


def translation(key):
    salt = getsalt()
    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': getSign(key, salt),
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }

    headers = {
        # 'Accept':'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding':'gzip, deflate',
        # 'Accept-Language':'zh-CN,zh;q=0.9',
        # 'Connection':'keep-alive',
        # 'Content-Length':'242',
        # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-48946618@10.169.0.84; JSESSIONID=aaaSABHpdlkKb6-n5HlTw; OUTFOX_SEARCH_USER_ID_NCOO=604160688.6131979; ___rl__test__cookies=1560340309390',
        # 'Host':'fanyi.youdao.com',
        # 'Origin':'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        # 'X-Requested-With':'XMLHttpRequest',
    }
    response = requests.post(url, data=data, headers=headers)
    infos = json.loads(response.text)
    if 'translateResult' in infos:
        try:
            result = infos['translateResult'][0][0]['tgt']
            # print(result)
        except:
            pass
    return result


print(translation("苹果"))


