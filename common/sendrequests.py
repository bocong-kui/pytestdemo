import allure
import requests
from pytestdemo.common.recordlog import logs
import json
from requests import utils
from pytestdemo.common.readyaml import ReadYamlData
import pytest

class SendRequest:
    def __init__(self):
        self.read=ReadYamlData()

    def send_request(self,**kwargs):
        cookie={}
        session=requests.session()
        try:
            result=session.request(**kwargs)
            set_cookie=requests.utils.dict_from_cookiejar(result.cookies)
            if set_cookie:
                # self.read.write_yaml_data(set_cookie)
                logs.info(f'cookie:{cookie}')
            logs.info(f'接口的实际返回信息:{result.text if result.text else result}')
        except requests.exceptions.ConnectionError:
            logs.error('接口连接服务器异常')
            pytest.fail('接口请求异常,可能是request的连接数过多或者请求数据过快导致程序报错')
        except requests.exceptions.HTTPError:
            logs.error('http异常')
            pytest.fail('http请求异常!')
        except requests.exceptions.RequestException as e:
            logs.error(e)
            pytest.fail('请求异常,请检查系统或数据是否正确')

        return result


    def run_main(self,name,url,case_name,header,method,cookies=None,file=None,**kwargs):
        '''
        接口请求
        :param method: 请求方法
        :param url: 接口地址
        :param data: 接口的请求参数
        :param header: 请求头
        :return: 返回json格式
        '''
        try:
            #收集报告日志信息
            logs.info(f'接口名称:{name}')
            logs.info(f'接口请求地址:{url}')
            logs.info(f'接口请求方式:{method}')
            logs.info(f'测试用例名称:{case_name}')
            logs.info(f'请求头:{header}')
            logs.info(f'Cookies:{cookies}')
            req_params=json.dumps(kwargs,ensure_ascii=False)
            if 'data' in kwargs.keys():
                logs.info(f'请求参数:{kwargs}')
                allure.attach(req_params,f'请求参数:{req_params}',allure.attachment_type.TEXT)
            elif 'json' in kwargs.keys():
                logs.info(f'请求参数:{kwargs}')
                allure.attach(req_params, f'请求参数:{req_params}', allure.attachment_type.TEXT)
            elif 'params' in kwargs.keys():
                logs.info(f'请求参数:{kwargs}')
                allure.attach(req_params, f'请求参数:{req_params}', allure.attachment_type.TEXT)
        except Exception as e:
            logs.info(e)

        response=self.send_request(method=method,url=url,headers=header,cookies=cookies,files=file,verify=False,**kwargs)
        return response






if __name__ == '__main__':
    method='get'
    url='http://127.0.0.1:8787/coupApply/cms/goodsList'
    data={
        'msgType':'getHandsetListOfCust',
        'page':1,
        'size':20
    }
    header={
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    send=SendRequest()
    res=send.run_main(method=method,url=url,data=data,header=None)
    print(res)