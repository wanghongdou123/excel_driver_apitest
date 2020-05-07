
import json
import requests

class RunMain:
    # 构造方法
    # def __init__(self, url, method, json=None, headers=None, data=None):
    #     self.res = self.run_main(url, method, json, headers, data)


    def get_main(self, url, data):
        res = requests.get(url, data).json()
        return res.text, res.status_code


    def post_main(self, url, json, headers):
        res = requests.post(url, json=json, headers=headers).json()
        return res.text, res.status_code,res.cookies


    def run_main(self, url, method, json=None, headers=None, data=None):
        res = None
        if method == 'GET':
            res = self.get_main(url, data)
        else:
            res = self.post_main(url, json, headers)
        return res













