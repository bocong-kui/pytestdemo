import random
import time
from readyaml import ReadYamlData
from pytestdemo.common.assertions import Assertions

class DebugTalk:
    def __init__(self):
        self.read = ReadYamlData()

    def get_extract_data_list(self, node_name, randoms=None):
        '''
             :param node_name:extract.yaml中的key值
             :param randoms:int类型,0:随机读取,-1:读取全部
             :return:
             '''
        data = self.read.get_extract_yaml(node_name)
        if randoms is not None:
            randoms = int(randoms)
            data_value = {
                randoms: self.get_extract_order_data(data,randoms),
                0: random.choice(data),
                -1: ','.join(data)
            }
            data = data_value[randoms]
        return data

    def get_extract_order_data(self, data, randoms):
        if randoms not in [0, -1, -2]:
            return data[randoms - 1]

    def get_extract_data(self, node_name, sec_node_name=None, randoms=None):
        '''

        :param node_name:extract.yaml中的key值
        :param sec_node_name:extract.yaml里面的key
        :param random:int类型,0:随机读取,-1:读取全部
        :return:
        '''
        data = self.read.get_extract_yaml(node_name, sec_node_name)
        # print('data的值从extract.yaml里面读取: ',data)
        if randoms is not None:
            randoms = int(randoms)
            data_value = {
                randoms: self.get_extract_order_data(data, randoms),
                0: random.choice(data),
                -1: ','.join(data),
                -2: ','.join(data).split(',')
            }
            data = data_value[randoms]
        return data

    def md5_params(self, params):
        return 'abcdefg123456' + str(params)

    def get_stamp_time(self):
        """获取当前时间戳，10位"""
        return time.time()


if __name__ == '__main__':
    debug = DebugTalk()
    print(debug.get_extract_data('product_id', 3))
