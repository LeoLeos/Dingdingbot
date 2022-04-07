# -*- coding: utf-8 -*-
"""
@Time: 2022/4/7 9:58
@Auth: LeoLucky(热衷开源的宝藏Boy)
@Project: dingdingbot
@File: dingdingbot.py
@IDE: PyCharm
@Email: 568428443@qq.com
@BlogSite: www.fangzengye.com
@motto: 学而知不足&写出简洁,易懂的代码是我们共同的追求
@Version:
@Desc:钉钉机器人bot
"""

import base64
import hashlib
import hmac
import time
from typing import List, Optional
from urllib.parse import quote_plus
import yaml

import requests

class DingRobot:
    """
    钉钉自定义机器人
    参考：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
    对不同的群进行不同消息的推送
    """

    def __init__(self, bot_name: str):
        """
        :param bot_name: 机器人名称
        """
        bot_info = self.__read_database_info("token.yaml")[bot_name]
        self.secret = bot_info["secret"]
        self.access_token = bot_info["access_token"]

    @staticmethod
    def __read_database_info(config_path):
        with open(config_path, 'r', encoding='utf-8') as fp:
            cont = fp.read()
        return yaml.safe_load(cont)

    @property
    def url(self):
        timestamp = round(time.time() * 1000)
        secret_enc = self.secret.encode("utf-8")
        string_to_sign = "{}\n{}".format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode("utf-8")
        hmac_code = hmac.new(
            secret_enc, string_to_sign_enc, digestmod=hashlib.sha256
        ).digest()
        sign = quote_plus(base64.b64encode(hmac_code))
        url = f"https://oapi.dingtalk.com/robot/send?access_token={self.access_token}&timestamp={timestamp}&sign={sign}"
        return url

    def send_text(
            self,
            text: str = None,
            mobiles: Optional[List[str]] = None,
            is_all: bool = False,
    ):
        """
        发送文本消息
        :param text: 文本消息内容
        :param mobiles: 被 @at 人的手机号
        :param is_all: 是否 @at 所有人
        :return:
        """
        res = requests.post(
            self.url,
            headers={"Content-Type": "application/json"},
            json={
                "msgtype": "text",
                "at": {
                    "atMobiles": mobiles or [],
                    "isAtAll": is_all,
                },
                "text": {"content": text},
            },
        )
        result = res.json()
        print(result)
        if result.get("errcode") == 0:
            print("发送成功！")

    def send_markdown(self, title=None, text=None, mobiles=None, is_all=False):
        """

        发送 Markdown 格式的消息
        :param title:
        :param text: 文本消息内容
        :param mobiles: 被 @at 人的手机号
        :param is_all: 是否 @at 所有人
        :return:
        """
        res = requests.post(
            self.url,
            headers={"Content-Type": "application/json"},
            json={
                "msgtype": "markdown",
                "markdown": {"title": title, "text": text},
                "at": {
                    "atMobiles": mobiles or [],
                    "isAtAll": is_all,
                },
            },
        )
        result = res.json()
        print(result)
        if result.get("errcode") == 0:
            print("发送成功！")

    def send_link(self, text, title, msg_url):
        res = requests.post(
            self.url,
            headers={"Content-Type": "application/json"},
            json={
                "msgtype": "link",
                "link": {
                    "text": text,
                    "title": title,
                    "picUrl": "",
                    "messageUrl": msg_url
                }
            },
        )
        result = res.json()
        print(result)
        if result.get("errcode") == 0:
            print("发送成功！")

    def send_action(self):
        pass

    def send_fend(self):
        pass