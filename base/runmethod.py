# post  get基类的封装

import requests
import json


class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
            # print(res.status_code)
        return res



    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        # print(res)
        return res


    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        # return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        # print(res)
        return res


# if __name__ == '__main__':
#     runmethod = RunMethod()
#     url = 'http://127.0.0.1:10086/add/'
#
#     data = {
#         "username": "admin",
#         "password": "admin"
#     }
#     headers = {"content-type": "application/json"}
#     rest = runmethod.run_main(method='POST',url=url, data=data, header=headers)
#     print(rest)

