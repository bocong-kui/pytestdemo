import configparser
from pytestdemo.conf.setting import FILE_PATH

class OperationConfig:
    '''封装读取ini配置文件'''

    def __init__(self,file_path=None):
        if file_path is None:
            self.file_path=FILE_PATH['conf']
        else:
            self.file_path=file_path
        self.conf=configparser.ConfigParser()
        try:
            self.conf.read(self.file_path,encoding='utf-8')
        except Exception as e:
            print(e)

    def get_section_for_data(self,section,option):
        '''
        :param section:ini头部值
        :param option:选项值的key
        :return:
        '''
        try:
            data=self.conf.get(section,option)
            return data
        except Exception as e:
            print(e)

    def write_section_for_data(self,section,option,value):
        '''

        :param section:
        :param option:
        :param value:
        :return:
        '''
        try:
            self.conf.set(section,option,value)
            with open(self.file_path,'w',encoding='utf-8') as rf:
                self.conf.write(rf)
        except Exception as e:
            print(e)

    def get_envi(self,option):
        '''获取接口服务器ip地址值'''
        return self.get_section_for_data('api_envi',option)

    def write_envi(self,option,value):
        self.write_section_for_data('api_envi',option,value)


    def get_section_redis(self,option):
        return self.get_section_for_data('REDIS',option)

        


if __name__ == '__main__':
    oper=OperationConfig()
    print(oper.get_envi('online'))
    oper.write_section_for_data('api_envi','online','https://www.bilibili.com')

def read_conf(section,option):
    conf=configparser.ConfigParser()
    conf.read(FILE_PATH['conf'])
    values=conf.get(section,option)
    return values


def write_conf(section,option,values):
    conf=configparser.ConfigParser()
    conf.read(FILE_PATH['conf'])
    conf.set(section,option,values)
    with open(FILE_PATH['conf'],'w',encoding='utf-8') as file:
        conf.write(file)


# print(read_conf('api_envi', 'host'))
# write_conf('MYSQL','port','3000')
