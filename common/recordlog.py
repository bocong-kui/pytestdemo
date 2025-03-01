import logging
import os
import time
from logging.handlers import RotatingFileHandler  # 按文件大小滚动备份

from pytestdemo.conf import setting

log_path = setting.FILE_PATH['LOG']
if not os.path.exists(log_path):
    os.mkdir(log_path)

logfile_name = f'{log_path}\\test.{format(time.strftime("%Y%m%d"))}.log'
# print(logfile_name)


class RecordLog:
    '''封装日志'''

    def output_logging(self):
        '''获取logger对象'''
        logger = logging.getLogger(__name__)
        # 防止打印重复log日志
        if not logger.handlers:
            logger.setLevel(setting.LOG_LEVEL)
            log_format = logging.Formatter(
                '%(levelname)s - %(asctime)s -%(filename)s:%(lineno)d - [%(module)s:%(funcName)s] -%(message)s')
            # 日志输出到指定文件
            fh=RotatingFileHandler(filename=logfile_name, mode='a', maxBytes=5242880,
                                backupCount=7, encoding='utf-8')  # maxBytes:控制单个日志文件的大小,单位是字节,backupCount:用于控制日志文件的数量
            fh.setLevel(setting.LOG_LEVEL)
            fh.setFormatter(log_format)

            #在将相应的handler添加到logger
            logger.addHandler(fh)

            #将日志输出到控制台上
            sh=logging.StreamHandler()
            sh.setLevel(setting.STREAN_LOG_LEVEL)
            sh.setFormatter(log_format)
            logger.addHandler(sh)

        return logger


apilog=RecordLog()
logs=apilog.output_logging()
