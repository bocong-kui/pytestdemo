from pytestdemo.conf.operationConfig import OperationConfig
from pytestdemo.common.recordlog import logs
import pymysql
import redis

conf = OperationConfig()


class RedisClient:
    """
        从Redis中读取,设置相关资源
    """
    def __init__(self):
        self.__redis_conf={
            'host':conf.get_section_redis('host'),
            'port':int(conf.get_section_redis('port')),
            'username':conf.get_section_redis('username'),
            'password':conf.get_section_redis('password'),
            'db':int(conf.get_section_redis('db')),
            'decode_responses':True
        }
        try:
            logs.info(f'连接到Redis服务器:ip:{self.__redis_conf.get("host")}')
            pool=redis.ConnectionPool(**self.__redis_conf)
            self.redis_cluster=redis.Redis(connection_pool=pool)
        except Exception as e:
            logs.error(f'redis连接失败:,{e}')
    def get(self,key):
        """
        获取Redis里面的数据
        :param key: Redis里面的键
        :return:
        """
        try:
            value=self.redis_cluster.get(key)
            return value
        except Exception as e:
            logs.error(f'从Redis中获取{key}失败,失败原因:{e}')
            raise


class RedisClient_another:
    def __init__(self):
        self.__redis_conf={
            'host':conf.get_section_redis('host'),
            'port':int(conf.get_section_redis('port')),
            'username':conf.get_section_redis('username'),
            'password':conf.get_section_redis('password'),
            'db':int(conf.get_section_redis('db')),
            'decode_responses':True
        }
        print(self.__redis_conf)
        self.redis_conn = redis.StrictRedis(**self.__redis_conf)

    def set(self, key, value):
        self.redis_conn.set(key, value)

    def get(self, key):
        return self.redis_conn.get(key)
    def hget(self,name,key):
        try:
            result=self.redis_conn.hget(name,key)
            logs.info(f'result:{result}')
            return result
        except Exception as e:
            logs.error(f'从Redis中获取{key}失败,失败原因:{e}')
            raise

    def hgetall(self, name):
        try:
            result = self.redis_conn.hgetall(name)
            logs.info(f'result:{result}')
            return result
        except Exception as e:
            logs.error(f'从Redis中获取{name}中所有键值对失败,失败原因:{e}')
            raise



if __name__ == '__main__':
    # my_redis=RedisClient()
    key='heima:user:1'
    # res=my_redis.get(key)
    # print(res)
    my_redis = RedisClient_another()
    res = my_redis.hget('userInfo','age')
    result=my_redis.hgetall('userInfo')
    print(type(result),result)
    print(res)
