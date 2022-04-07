# DingdingBot

钉钉消息通知机器人

## 如何使用

使用 `ding_inform` 装饰器装饰函数, 检查该函数运行情况

```
@ding_inform("bot1", "测试")
def test():
    pass
```

自定义钉钉机器人文档 [https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)