import jsonpath

from pytestdemo.common.recordlog import logs
from pytestdemo.readyaml import get_testcase_yaml
import os
import pathlib


class Assertions:
    """
    接口断言模式,支持
    1.字符串包含
    2.结果相等断言
    3.结果不相等断言
    4.断言接口返回值里面的任意一个值
    5.数据库断言
    """

    def contains_assert(self, value, response, status_code):
        '''
        第一种模式,字符串包含断言,断言预期结果的字符串是否包含在接口的实际返回结果当中
        :param value: 预期结果,yaml文件当中validation关键字下的结果
        :param response:
        :param status_code:
        :return:
        '''
        #断言状态表示,0代表成功,其他代表失败
        flag=0
        for assert_key, assert_value in value.items():
            print(assert_key, assert_value)
            if assert_key == 'status_code':
                if assert_value != status_code:
                    flag+=1
                    logs.error(f'contains断言失败，接口返回码【{status_code}】不等于【{assert_value}】')
            else:
                resp_list = jsonpath.jsonpath(response, f'$..{assert_key}')
                if isinstance(resp_list[0],str):
                    resp_list=''.join(resp_list)
                    if resp_list:
                        if assert_value in resp_list:
                            logs.info(f'字符串包含断言成功:预期结果为:【{assert_value}】,实际结果为:【{resp_list}】')
                        else:
                            flag+=1
                            logs.error(f'响应文本断言结果:预期结果为:【{assert_value}】,实际结果为:【{resp_list}】')
        return flag

    def equal_assert(self):
        """相等模式"""


    def not_equal_assert(self):
        """不相等模式"""

    def assert_result(self,expected,respone,status_code):
        """
        断言模式,通过all_flag标记
        :param expected: 预期结果
        :param respone: 实际结果
        :param status_code: 接口实际返回状态码
        :return:
        """
        all_flag=0
        # 0代表成功,其他代表失败
        try:
            for yq in expected:
                for key,value in yq.items():
                    if key =='contains':
                        flag=self.contains_assert(value,respone,status_code)
                    elif key=='eq':
                        self.equal_assert(value,respone,status_code)

            assert all_flag==0
            logs.info('测试成功!')
        except Exception as e:
            logs.error('测试失败')
            logs.error(f'异常信息{e}')
            assert all_flag==0




if __name__ == '__main__':
    # print(os.path.join(os.path.dirname(os.path.dirname(__file__)),'testCase\login','login.yaml'))

    data = get_testcase_yaml(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testCase\login', 'login.yaml'))
    value = jsonpath.jsonpath(data, '$..validation')[0]
    response = {"error_code": None, "msg": "登录成功", "msg_code": 200, "orgId": "6140913758128971280",
                "token": "aDb9D3aDCECa8dCcb99ad6dbb0753", "userId": "3202566944016373375"}
    ass = Assertions()
    for i in value:
        for k, v in i.items():
            ass.contains_assert(v, response, 200)
