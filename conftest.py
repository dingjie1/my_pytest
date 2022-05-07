import pytest
# from common.CRM import CRM
# import json
#
# crm = CRM()
#
# def prepare_for_test():
#     # 用于处理一些运行前的预操作,比如登录获取token，并赋值token给所有请求
#     print('prepare_for_test() starting print...')
#     crm.request.headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json, text/plain, */*",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
#
#     }
#
# prepare_for_test()


@pytest.fixture(scope='session')
def data1():
    print("会话级")

@pytest.fixture(scope='module')
def data2():
    print("模块级")

@pytest.fixture(scope='class')
def data3():
    print("类级")

@pytest.fixture(scope='function')
def data4():
    print("函数级")
