# _*_ coding: utf-8 _*_

"""
本项目其他文件为赠送代码，仅供学习交流使用，不提供技术支持
赠送的代码有些需要安装第三方包，请自行查阅资料安装，
如果实在遇到困难安装不上的，本店提供有偿安装服务
"""

import time

from python_celery import add

if __name__ == "__main__":
    result = []
    for i in range(10):
        result.append(add.delay(i, i))
    print("----", time.time())
    for index, item in enumerate(result):
        print(index, item.get())
    print("----", time.time())
