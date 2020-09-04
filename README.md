# dingTalkRobotHelper
钉钉机器人小助手

# 要求

- python 3

- docker【可选】
  
# local_setting.py

```
config = {
    'name': '钉钉小助手',
    'robots': [{
        'name': '机器人1',
        'key': 'any_str',
        'access_token': '',
        'access_secret': ''
        }... 如果有多个机器人，继续配置即可]
}
```

- 启动命令

`pip install -r requirement.txt`

`python app.py`