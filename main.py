import urllib.request
import urllib.parse
import random
import time
import hashlib
import gzip
import json
'''
Host: fanyi.youdao.com
Connection: keep-alive
Content-Length: 200
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://fanyi.youdao.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://fanyi.youdao.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

'''


content=input("请输入需要翻译的单词：")
# 去掉_o能快速实现，但是这可能使用的是一个较老的接口，结果存在一定问题。
# url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
client= 'fanyideskweb'
ctime=int(time.time()*1000)
salt = str(ctime + random.randint(0,9))   #randint包括上下限，randrange不包括上限
key = 'ebSeFb%=XZ%T[KZ)c(sy!'
sign = hashlib.md5((client+ content + salt + key).encode('utf-8')).hexdigest()
# print(salt)
# print(sign)

headers={
"Accept":"application/json, text/javascript, */*; q=0.01",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Content-Length":"200",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Cookie":"OUTFOX_SEARCH_USER_ID=1485688130@117.136.8.67; OUTFOX_SEARCH_USER_ID_NCOO=175269500.70791978; JSESSIONID=aaaXRZtGU0RMC6AHGGrlw; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcjiMbAFn0GQ7x9sHrlw; ___rl__test__cookies="+str(ctime),
"Host":"fanyi.youdao.com",
"Origin":"http://fanyi.youdao.com",
"Proxy-Connection":"keep-alive",
"Referer":"http://fanyi.youdao.com/",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
"X-Requested-With":"XMLHttpRequest"
}

formdata={
"i":content,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":salt,
"sign":sign,
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTIME",
"typoResult":"false"
}

data=urllib.parse.urlencode(formdata).encode('utf-8')    #将字典转为url形式（带&）
# 通过urllib.request.Request()构造一个请求对象
request=urllib.request.Request(url,data=data,headers=headers)

# 服务器返回的类文件对象支持Python文件对象的操作方法
response=urllib.request.urlopen(request)

with gzip.open(response, 'rb') as f:
    response = f.read()
        # response=response.read().decode('utf-8')
    # 转成json文件
    target = json.loads(response)
    print("翻译结果：")
    result = target['translateResult'][0][0]['tgt']
    print(result)
