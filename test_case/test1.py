import pytest
from conftest import *
import allure

@allure.epic('测试标签')
@allure.feature('测试模块')
class Test_set:

    def login(self):
        print("login...")

    @pytest.mark.dependency()
    @allure.testcase(url='www.baidu.com', name='百度')
    @allure.story('test01-story')
    @allure.title('test01标题')
    @pytest.mark.run(order=2)
    def test_01(self):
        print("+++test01")
        assert False

    @pytest.mark.dependency(depends='test01')
    @allure.story('test02-story')
    @allure.title('test02标题')
    @pytest.mark.run(order=1)  # pytest-ordering指定执行顺序
    def test_02(self):
        print("+++test02")

    @allure.story('test03-story')
    @allure.title('test03标题')
    @pytest.mark.skip   # 跳过本条用例
    @pytest.mark.parametrize('a',[1,2,3])
    def test_03(self,a):
        '''用例3描述'''
        with allure.step('用例3步骤'):
            print('用例3步骤')
        print("+++test03+++",a)

    @allure.issue(url='www.baidu.com',name='bug')
    @allure.story('test04-story')
    @allure.title('test04标题')
    @pytest.mark.parametrize('b,c',[(4,5)])
    def test_04(self,b,c):
        '''用例4描述'''
        print("+++test04+++",b,c)
        assert b ==4 and c == 5

    # def setup(self):
    #     print("\n每条用例运行前执行")
    #
    # def teardown(self):
    #     print("\n每条用例运行后执行")
    #
    # def setup_class(self):
    #     print("\n测试类运行前执行")
    #
    # def teardown_class(self):
    #     print("\n测试类运行前执行")

    @pytest.mark.usefixtures('data1')
    def test_05(self,data1):
        print("+++test05+++")

    @pytest.mark.usefixtures('data2')
    def test_06(self,data2):
        print("+++test06+++")

    @pytest.mark.usefixtures('data3')
    def test_07(self,data3):
        print("+++test07+++")

    @pytest.mark.usefixtures('data4')
    def test_08(self,data4):
        print("+++test08+++")


if __name__ == "__main__":

    pytest.main(['-v','-s','test1.py'])
