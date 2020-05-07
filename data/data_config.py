# 常量封装

class global_var:
    # case_id
    Id = '0'
    module_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    depend_to = '9'
    data = '10'
    expect = '11'
    result = '12'


# 获取caseid
def get_id():
    return global_var.Id

# 定义获取name
def get_module_name():
    return global_var.module_name


# 获取url
def get_url():
    return global_var.url

# 获取是否运行
def get_run():
    return global_var.run

# 获取请求方式
def get_request_way():
    return global_var.request_way

# 获取header
# def get_header():
#     return global_var.header

# 获取header
def get_header_value():
    return global_var.header


# 获取case_depend
def get_case_depend():
    return global_var.case_depend

# 获取数据依赖
def get_data_depend():
    return global_var.data_depend

# 获取字段依赖
def get_field_depend():
    return global_var.field_depend

# 获取依赖添加地
def get_depend_to():
    return global_var.depend_to

# 获取请求数据
def get_data():
    return global_var.data

# 获取预期结果
def get_expect():
    return global_var.expect

# 获取实际结果
def get_result():
    return global_var.result





