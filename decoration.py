# -*- coding: utf-8 -*-
"""
@Time: 2022/4/7 9:57
@Auth: LeoLucky(热衷开源的宝藏Boy)
@Project: dingdingbot
@File: decoration.py
@IDE: PyCharm
@Email: 568428443@qq.com
@BlogSite: www.fangzengye.com
@motto: 学而知不足&写出简洁,易懂的代码是我们共同的追求
@Version:
@Desc: 钉钉机器人装饰器
"""

from dingdingbot import DingRobot
from functools import wraps
import traceback
import datetime

def ding_inform(robot: str, info: str):
    """
    robot: 机器人名称
    info: 通知信息
    作用: 添加一个钉钉消息通知机器人装饰器, 应用与检查该函数是否报错
    """
    def ding_inform(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            ding = DingRobot(robot)
            try:
                function(*args, **kwargs)
                t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ding.send_text("Success!!!\n时间: {} ".format(t) + info)
            except Exception as e:
                t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ding.send_text("Bug!!!\n时间: {} ".format(t) + info + "报错函数: {},\n具体位置: {},\n报错原因: {}".format(function.__name__, traceback.format_exc(), e))
        return wrapper
    return ding_inform