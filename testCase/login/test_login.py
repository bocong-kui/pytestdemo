import allure
import pytest
import time
from pytestdemo.common.readyaml import get_testcase_yaml
from pytestdemo.common.sendrequests import SendRequest
from pytestdemo.common.recordlog import logs
from pytestdemo.base.apiutil import BaseRequests

# scope 表示被@pytest.fixture标记的方法作用域,他的值主要有4个,function(默认),class,module,package/session
# params  参数化 支持格式有列表 元组 字典
# autouse 自动使用
# ids 当使用params参数化时候,给每一值设置一个变量,意义不大
# name
# @pytest.fixture(scope='function',autouse=True,params=['子','丑','寅','卯'],ids=['shu','niu','hu','tu'],name='test3')
# def fixture_test(request):
#     '''前后置处理'''
#     # print('------------接口测试开始--------------')
#     # yield
#     # print('------------接口测试结束---------------')
#     return request.param

@allure.feature('登录接口')
class TestLogin:

    # def setup_class(self):
    #     '''在所有测试用例执行前只执行一次'''
    #     "类的初始化工作,比如说创建对象，创建数据库"
    #
    # def setup_method(self):
    #     print('在每个测试方法运行前都要执行我的代码块')

    # @pytest.mark.run(order=2)
    # @pytest.mark.parametrize('params',[{"name":"小张"},{"name":"小李"}])
    @allure.story('用户名和密码登录正常校验')
    @pytest.mark.parametrize('params',get_testcase_yaml('./testCase/login/login.yaml'))
    def test_case01(self,params):
        BaseRequests().specification_yaml(params)

    # @allure.story('用户名和密码登录错误校验')
    # @pytest.mark.parametrize('params', get_testcase_yaml('./testCase/login/login.yaml'))
    # def test_case02(self, params):
    #     BaseRequests().specification_yaml(params)
    # @pytest.mark.run(order=3)
    # @pytest.mark.skip
    # @pytest.mark.parametrize('params', get_testcase_yaml('./testCase/login/login.yaml'))
    # def test_case02(self, params):
        # url = params['baseInfo']['url']
        # new_url = f'http://127.0.0.1:8787{url}'
        # logs.info(f'获取到接口地址:{new_url}')
        # method = params['baseInfo']['method']
        # logs.info(f'获取到接口方法:{method}')
        # headers = params['baseInfo']['header']
        # data = {'user_name':'test02','passwd':'123'}
        # send = SendRequest()
        # res = send.run_main(url=new_url, data=data, header=None, method=method)
        # print('接口实际返回值: ', res)
        # assert res['msg'] == '登录成功'
        # BaseRequests().specification_yaml(params)

    # @pytest.mark.run(order=1)
    # @pytest.mark.usermanager
    # @pytest.mark.smoke
    # def test_case03(self):
    #     print('用例3')

    # def teardown_method(self):
    #     '''后置处理'''
    #     print('在每个测试方法运行后都要执行我的代码块')
    #
    # def teardown_class(self):
    #     print('关闭数据库的连接')



# class TestLogout:
#
#     # def setup_class(self):
#     #     '''在所有测试用例执行前只执行一次'''
#     #     "类的初始化工作,比如说创建对象，创建数据库"
#     #
#     # def setup_method(self):
#     #     print('在每个测试方法运行前都要执行我的代码块')
#
#     # @pytest.mark.run(order=2)
#     def test_case01(self):
#         print('用例1')
#
#     # @pytest.mark.run(order=3)
#     # @pytest.mark.skip
#     def test_case02(self):
#         print('用例2')
#
#     # @pytest.mark.run(order=1)
#     # @pytest.mark.usermanager
#     # @pytest.mark.smoke
#     def test_case03(self):
#         time.sleep(2)
#         print('用例3')
