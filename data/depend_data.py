from util.operation_excel import  OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
import json

class DependdentData:
    def __init__(self,id):
        self.id = id
        self.opera_excel =  OperationExcel()
        self.data = GetData()

    '''
    通过case_id去获取该case_id的整行数据
    '''
    def get_case_line_data(self,id):
        rows_data = self.opera_excel.get_row_data(self.id)
        return rows_data

    # 执行依赖测试获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.id)
        # request_data = self.data.get_data_for_json(row_num)
        request_data = json.dumps(self.data.get_request_data(row_num))
        header = self.data.get_is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_url(row_num)
        print('row_num:',row_num,'request_data:',request_data,'header:',header,'method:',method,'url:',url)
        res = run_method.run_main(method,url,request_data,header)       # order
        return json.loads(res.text)




    # 根据依赖的key获取执行依赖case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)       # depend_data:text
        response_data = self.run_dependent()              # response_data   {"code":0,"text":"order"}

        # 获取匹配的数据  match.value
        json_exe = parse(depend_data)                 # text   <class 'jsonpath_rw.jsonpath.Fields'>
        madle = json_exe.find(response_data)              # []
        print('madle:',madle)
        return [math.value for math in madle][0]


if __name__ == '__main__':
    dependdentdata = DependdentData('mock002')
    dependdentdata.run_dependent()
    dependdentdata.get_data_for_key(5)













