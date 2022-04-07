# -*- coding: utf-8 -*-
"""
@Time: 2022/4/7 10:11
@Auth: LeoLucky(热衷开源的宝藏Boy)
@Project: dingdingbot
@File: test.py
@IDE: PyCharm
@Email: 568428443@qq.com
@BlogSite: www.fangzengye.com
@motto: 学而知不足&写出简洁,易懂的代码是我们共同的追求
@Version:
@Desc:测试
"""

from decoration import ding_inform

@ding_inform("bot1", "测试")
def test():
    pass

if __name__ == '__main__':
    test()
    pass