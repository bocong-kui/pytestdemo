import pytest
from pytestdemo.common.recordlog import logs
from pytestdemo.common.readyaml import ReadYamlData

'''
    function:每一个函数或方法都会调用
    class:每一个类调用一次,一个类中可以有多个方法
    module:每一个.py文件调用一次,该文件内又有多个function和class
    session:是多个文件调用一次,可以跨.py文件调用,每个.py文件就是module,整个会话只会运行一次
    autouse:默认是false，不会自动执行,需要手动调用,为true可以自动执行,不需要调用
'''

# read = ReadYamlData()
#
#
# @pytest.fixture(scope='session', autouse=True)
# def clear_extract_data():
#     read.clear_yaml_data()


@pytest.fixture(scope='session', autouse=True)
def fixture_test(request):
    '''前后置处理'''
    ReadYamlData().clear_yaml_data()
    logs.info('------------接口测试开始--------------')
    yield
    logs.info('------------接口测试结束---------------')
    # return request.param
