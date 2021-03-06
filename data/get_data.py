# 封装获取接口数据

from util.operation_excel import OperationExcel
from data import data_config
from util.operation_json import OperationJson
import json

class GetData:
    def __init__(self):
        self.opera_exel = OperationExcel()

    # 获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_exel.get_lines()


    # 获取id
    def get_id(self, row):
        col = int(data_config.get_id())
        id = self.opera_exel.get_cell_value(row, col)
        return id


    # 获取case_name
    def case_name(self,row):
        col = int(data_config.get_module_name())
        case_name = self.opera_exel.get_cell_value(row,col)
        return case_name


    # 获取url
    def get_url(self, row):
        col = int(data_config.get_url())
        url = self.opera_exel.get_cell_value(row, col)
        return url


    # 获取是否执行
    def get_is_run(self,row):
        col = int(data_config.get_run())
        run_model = self.opera_exel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag


    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_request_way())
        request_method = self.opera_exel.get_cell_value(row, col)
        return request_method


    # 是否携带header
    def get_is_header(self,row):
        col = int(data_config.get_header_value())
        header = self.opera_exel.get_cell_value(row,col)
        if header != 'no':
            if header != '':
                return json.loads(header)
        else:
            return None


    # 获取请求数据
    def get_request_data(self,row):
        col = int(data_config.get_data())
        # print(col)
        data = self.opera_exel.get_cell_value(row,col)
        if data == '':
            return None
        return json.loads(data)
        # return data



    # 通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperationJson()
        test = json.dumps(self.get_request_data(5))
        print(test,'111')
        # request_data = opera_json.get_data(json.dumps(self.get_request_data(row)))
        request_data = opera_json.get_data(json.dumps(self.get_request_data(row)))
        return request_data



    # 获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.get_expect())
        expect = self.opera_exel.get_cell_value(row,col)
        if expect == '':
            return None
        return expect


    # 写入
    def write_result(self,row,value):
        col = int(data_config.get_result())
        self.opera_exel.write_value(row,col,value)


    # 获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data_config.get_data_depend())
        depend_key = self.opera_exel.get_cell_value(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key


    # 判断是否有case依赖
    def is_depend(self,row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.opera_exel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id


    # 获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data_config.get_field_depend())
        depend_field = self.opera_exel.get_cell_value(row,col)
        if depend_field == "":
            return None
        else:
            return depend_field


    # 获取依赖添加地
    def get_to_depend(self,row):
        col = int(data_config.get_depend_to())
        depend_to = self.opera_exel.get_cell_value(row,col)
        if depend_to == "":
            return None
        else:
            return depend_to


# #
# if __name__ == '__main__':
#     getdata = GetData()
#     print(getdata.get_request_data(1))
#     # w = getdata.get_is_header(1)
#     print(type(w))
#     # print(getdata.get_data_for_json(1))
#     print(getdata.get_data_for_jso n(4))
#     print(getdata.get_request_data(5))


