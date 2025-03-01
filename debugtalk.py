import random

from readyaml import ReadYamlData


class DebugTalk:
    def __init__(self):
        self.read = ReadYamlData()

    def get_extract_order_data(self, data, randoms):
        if randoms not in [0, -1, -2]:
            return data[randoms - 1]

    def get_extract_data(self, node_name, randoms=None):
        '''

        :param node_name:extract.yaml中的key值
        :param random:随机读取extract.yaml 中的数据
        :return:
        '''
        data = self.read.get_extract_yaml(node_name)
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
        return 'abcdefg123456'+str(params)


if __name__ == '__main__':
    debug = DebugTalk()
    print(debug.get_extract_data('product_id', 3))
