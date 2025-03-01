import requests

class SendRequest:
    def __init__(self):
        pass

    def get(self,url,data,header):
        '''

        :param url:
        :param data:
        :param header:
        :return:
        '''
        if header is None:
            res=requests.get(url=url,params=data,verify=False)
        else:
            res=requests.get(url=url,params=data,headers=header,verify=False)
        return res.json()
    def post(self,url,data,header):
        '''
        :param url:
        :param data:verify=False忽略SSL证书验证
        :param header: 接口的请求头
        :return: 返回json格式
        '''
        if header is None:
            res=requests.post(url,data,verify=False)
        else:
            res=requests.post(url,data,headers=header,verify=False)

        return res.json()

    def run_main(self,method,url,data,header):
        '''
        接口请求
        :param method: 请求方法
        :param url: 接口地址
        :param data: 接口的请求参数
        :param header: 请求头
        :return: 返回json格式
        '''
        res=None
        if method.upper()=='GET':
            res=self.get(url,data,header)
        elif method.upper()=='POST':
            res=self.post(url,data,header)
        else:
            print('暂时只支持get/post请求!')
        return res



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