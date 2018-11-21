import json
from urllib.parse import urlencode
from urllib.request import urlopen
import datetime

from .utils import do_reply

def request1( m="GET"):

    url = "http://api.juheapi.com/japi/toh"
    appkey = "d5ed83caf50b33158b580e865ff46424"
    params = {
        "key": appkey,
        "v": "1.0",
        'month':datetime.datetime.now().month,
        'day':datetime.datetime.now().day
    }
    params = urlencode(params)
    if m == "GET":
        f = urlopen("%s?%s" % (url, params))
    else:
        f = urlopen(url, params)
    content = f.read()
    res = json.loads(content)
    ress = ''
    pic = ''
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            res = res['result'][1]
            ress = res['title'] + ':' + res['des'] +':'+ res['pic']

            print(ress)
        return ress




def request2( m="GET",):
    url = "http://web.juhe.cn:8080/constellation/getAll"

    params = {
        "key":"37d2ff35b6b187bda287085b880fd731",
        "consName": '处女座',
        "type": "today",
    }
    params = urlencode(params)
    if m == "GET":
        f = urlopen("%s?%s" % (url, params))
    else:
        f = urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    ress = ''
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            ress = res
            print(ress)
        return ress


if __name__ == '__main__':
    request1()

if __name__== '__main__':
    request2()