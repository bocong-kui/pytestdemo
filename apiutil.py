from readyaml import ReadYamlData,get_testcase_yaml
import json
from debugtalk import DebugTalk

class BaseRequests:

    def __init__(self):
        self.read=ReadYamlData()

    def replace_load(self,data):
        '''yaml文件替换解析由${}格式的数据'''
        str_data=data
        if not isinstance(data,str):
            str_data=json.dumps(data,ensure_ascii=False)

        for i in range(str_data.count('${')):
            if "${" in str_data and "}" in str_data:
                start_index=str_data.index('$')
                end_index=str_data.index('}',start_index)
                # print(start_index,end_index)
                ref_all_params=(str_data[start_index:end_index+1])
                print(ref_all_params)
                #取出函数名
                func_name=ref_all_params[2:ref_all_params.index('(')]
                #取出函数里面的参数值
                funcs_params=ref_all_params[ref_all_params.index('(') + 1:ref_all_params.index(")")]

                #传入替换的参数获取对应的值
                # print('yaml文件替换解析前: ', str_data)
                extract_data=getattr(DebugTalk(),func_name)(*funcs_params.split(',') if funcs_params else '')
                print(extract_data)

                str_data=str_data.replace(ref_all_params,str(extract_data))
                print('yaml文件替换解析后: ', str_data)

        # 还原数据
        if data and isinstance(data,dict):
            data=json.loads(str_data)
        else:
            data=str_data
        return data


if __name__ == '__main__':
    data=get_testcase_yaml('login.yaml')[0]
    print(data)
    base=BaseRequests()
    res=base.replace_load(data)
    print(res)
