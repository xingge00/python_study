import re

# 浏览器上的请求头信息转为JSON格式的字符串
headers_str = """
i: apple
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15603403093934
sign: 6862502d689022158f6373c867c4c62b
ts: 1560340309393
bv: c4e95e621267f4d4577f554f2869b772
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION
"""

pattern = '^(.*?): (.*)$'
for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\': \'\\2\',', line))
