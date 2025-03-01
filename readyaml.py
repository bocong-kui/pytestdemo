# -*- coding:utf-8 -*-
import json
import traceback

import yaml
import os

def read_yaml(file):
    with open(file,'r',encoding='utf-8') as f:
        values=yaml.load(f,Loader=yaml.FullLoader)
        return values


def get_testcase_yaml(file):
    '''
    获取yaml文件的数据
    :param file:yaml文件的路径
    :return:
    '''
    try:
        with open(file,'r',encoding='utf-8') as f:
            yaml_data=yaml.safe_load(f)
            return yaml_data
    except Exception as e:
        print(e)



class ReadYamlData:
    '''
        读取yaml数据,以及写入数据到yaml文件
    '''
    def __init__(self,yaml_file=None):
        if yaml_file:
            self.yaml_file=yaml_file
        else:
            self.yaml_file='login.yaml'

    def write_yaml_data(self,value):
        '''
        写入数据到yaml文件
        :param value: (dict)写入的数据
        :return:
        '''
        file_path='./extract.yaml'
        if not os.path.exists(file_path):
            os.system(file_path)
        try:
            file=open(file_path,'a',encoding='utf-8')
            if isinstance(value,dict):
                write_data=yaml.dump(value,allow_unicode=True,sort_keys=False)
                file.write(write_data)
            # with open(file_path,'a',encoding='utf-8') as f:
            #     if isinstance(value,dict):
            #         write_data=yaml.dump(value,allow_unicode=True,sort_keys=False)
            #         f.write(write_data)
            else:
                '写入到[extract.yaml]的数据必须为字典类型:'
        except Exception as e:
            print(str(traceback.format_exc()))

        finally:
            file.close()

    def get_extract_yaml(self,node_name):
        '''
        读取接口提取的变量值
        :param node_name:yaml文件中key值
        :return:
        '''
        if os.path.exists('extract.yaml'):
            pass
        else:
            print('extract.yaml不存在')
            file=open('extract.yaml','w')
            file.close()
            print('extract.yaml创建成功!')

        with open('extract.yaml','r',encoding='utf-8') as rf:
            extract_data=yaml.safe_load(rf)
            # print(extract_data)
            return extract_data[node_name]






if __name__ == '__main__':
    res=get_testcase_yaml('./login.yaml')[0]

    url=res['baseInfo']['url']
    new_url=f'http://127.0.0.1:8787{url}'

    method=res['baseInfo']['method']
    header=res['baseInfo']['header']
    data=res['testCase'][0]['data']
    from sendrequests import SendRequest
    send=SendRequest()
    res=send.run_main(method=method,url=new_url,data=data,header=None)
    print(res)
    token=res.get('token')
    write_data={}
    write_data['token']=token

    print(token)
    read=ReadYamlData()
    read.write_yaml_data(write_data)
    # json_str=json.dumps(res,ensure_ascii=False)
    # print(json_str)

    #json反序列化,其实就是将字符串类型转换为字典类型
    # json_dict=json.loads(json_str)
    # print(json_dict)
    # print(type(json_dict))

    res2=read.get_extract_yaml('token')
    print(res2)


# print(read_yaml('./login.yaml'))
# print(get_testcase_yaml('./login.yaml'))