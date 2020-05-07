# 主程序入口封装
import sys
sys.path.append('/Users/wanghongdou/PycharmProjects/apiDemoTest')
print('11111')
print(sys.path)
print('222222')

from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
import json
from data.depend_data import DependdentData
from util.send_email import SendEmail



class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil
        self.send_mai = SendEmail()

    # 程序执行的主入口
    def go_on_run(self):
        res = None
        pass_count = []
        file_count = []
        skip_count = []
        rows_count = self.data.get_case_lines()

        for i in range(1,rows_count):
            print('第',i,'条case')
            id = self.data.get_id(i)
            print('id:',id)
            url = self.data.get_url(i)
            print('url:',url)
            method = self.data.get_request_method(i)
            print('method:',method)
            is_run = self.data.get_is_run(i)
            print('is_run:',is_run)
            # data = self.data.get_data_for_json(i)
            # print('data:',data)
            data = self.data.get_request_data(i)
            data = json.dumps(data)
            print('data:', data,type(data))
            expect = self.data.get_expect_data(i)
            print('expect:',expect)
            header = self.data.get_is_header(i)
            print('header:',header,type(header))
            depend_case = self.data.is_depend(i)
            depend_to = self.data.get_to_depend(i)
            print('depend_to:',depend_to,type(depend_to))


            if is_run:

                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    # 获取响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)     # <class 'str'>   order

                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)     # text

                    # 拼接进去
                    if depend_to == 'H':
                        header[depend_key] = depend_response_data
                        # print('header[depend_key]:',header[depend_key],type(header[depend_key]))
                    elif depend_to == 'B':
                        data = json.loads(data)
                        data[depend_key] = depend_response_data
                        data = json.dumps(data)
                    else:
                        pass


                res = self.run_method.run_main(method, url, data, header)
                print(res.text,'----------')


                # if self.com_util.is_contain(self,expect,res):

                if expect in res.text:
                    # print(i,"测试通过",expect,res.text)
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:
                    # print(res.status_code)
                    # print(i,"测试失败",expect,res.text)
                    self.data.write_result(i, res.text)
                    file_count.append(i)

            else:
                skip_count.append(i)

            i += 1


        print('通过：',len(pass_count),'失败：',len(file_count),'跳过：',len(skip_count))
        self.send_mai.send_main(pass_count,file_count,skip_count)

if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()












