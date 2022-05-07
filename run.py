import os
import shutil

import allure
import pytest

def run(*args, **paths):
    #执行参数
    # __file__返回文件当前目录包含文件名，dirname返回文件路径即去掉当前文件名，这里返回到my_pytest目录
    allure_dir = os.path.join(os.path.dirname(__file__), 'output', 'allure')
    allure_result = os.path.join(os.path.dirname(__file__), 'output', 'result')

    param = ['-s', '-v',
            '--alluredir={}'.format(allure_dir), #生成alluer报告
            '--cache-clear'  # 清空缓存
            ]

    param.extend(paths.values())  # 添加脚本加载路径
    try:
        for i in args:
            param = param + i  # 添加指定执行顺序脚本列表
    except IndexError as e:
        print(e)
        print("自定义测试套件不存在")

    print("param=", param)

    pytest.main(param)  # 执行测试

    # 生成allure 本地在线报告
    os.system("allure generate {allure_dir} -o {allure_result} --clean".format(allure_dir=allure_dir,
                                                                               allure_result=allure_result))
    # 打开展示测试报告
    os.system("allure open {allure_result}".format(allure_result=allure_result))

if __name__ == '__main__':
    if os.path.exists('./output'):
        shutil.rmtree('./output')  # 如果存在output目录，则递归删除该目录及其下所有内容
    run(path0=os.path.join(os.path.dirname(__file__), 'test_case','test1.py'))
