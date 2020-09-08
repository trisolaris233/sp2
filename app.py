from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

@app.route('/same', methods=['POST', 'GET'])
def same():
    url = "https://api.same01.com/user/contact/senses"
    header = {
        'Host': 'api.same01.com',
        'Machine': 'ios|301|iOS 13.5|iPhone|750|1536',
        'Authorization': 'Token 1599544064-VTkenKPhFNBzOErp-16521233',
        'X-Same-Request-ID': '26E10849-5771-4CA6-8286-B01D376F656A',
        'encode_type': 'json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Advertising-UUID': 'CA61334A-0EF3-47C5-B26A-0E8CE1D49F51',
        'Accept-Language': 'zh-Hans-CN;q=1, zh-Hant-CN;q=0.9',
        'X-same-Device-UUID': 'F54C972F-99DD-423A-AAAB-3945FB033AE7',
        'Accept': 'application/json',
        'User-Agent': 'same/869 (iPhone; iOS 13.5; Scale/2.00)',
        'Connection': 'keep-alive',
        'timezone': 'Asia/Shanghai'
    }
    token = 2333
    form = request.headers.get("token")

    res = {
        "code": "200",
        "res": "",
        "msg": "OK"
    }
    if token == int(request.headers.get("token")): 
        try:
            req = requests.get(url, headers=header)
            jsonmsg = req.json()
            res['res'] = jsonmsg
                    
        except requests.ConnectionError:
            res['code'] = 1
            res['msg'] = "ConnectionError"

        except requests.Timeout:
            res['code'] = 2
            res['msg'] = "Timeout"
            pass
        except requests.HTTPError:
            res['code'] = 3
            res['msg'] = "HTTPError"

        return jsonify(res)

    res['code']=4
    res['msg'] = "Wrong Token"
    return jsonify(res)





