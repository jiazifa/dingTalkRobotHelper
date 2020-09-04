import sys
from flask import Flask, render_template, request
from collections import namedtuple

Robot = namedtuple('Robot', ['name', 'key', 'access_token', 'access_secret'])

def parse_params(request):
    """  从一个Request实例中解析params参数
    Args:
        request: flask.request 实例对象
    Return: 一个解析过的字典对象，如果没有解析出，则返回一个空的字典对象
    """
    r = request
    d = {}
    if r.method == "GET":
        if json:= r.args or r.get_json():
            d = dict(json)

    if r.method == "POST":
        if json:= r.get_json() or r.args:
            d = dict(json)

    if not d:
        d = dict(r.values)
    return d

def find_robot_by_key(robots, key):
    rs = list([Robot(r['name'], r['key'], r['access_token'], r['access_secret']) for r in robots])
    result = list(filter(lambda r: r.key == key, rs))
    return result[-1]



app = Flask(__name__, static_folder='static', template_folder='templates')

config = {
    'name': '钉钉小助手',
    'robots': [{
        'name': '',
        'key': '',
        'access_token': '',
        'access_secret': '',
    }]
}

try:
    import local_setting
    config.update(local_setting.config)
except ImportError:
    pass

@app.route('/')
def index():
    return render_template('index.html', config=config)

@app.route('/execute', methods=["POST"])
def execute():
    params = parse_params(request)
    key = str(params['key'])
    content = str(params['content'])
    atAll = bool(params['atAll'])
    robot = find_robot_by_key(config['robots'], key)
    if not robot:
        return {'status': 'error', 'msg': '未找到机器人'}
    try:
        from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, FeedLink, CardItem

        new_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=' + robot.access_token
        xiaoding = DingtalkChatbot(new_webhook, secret=robot.access_secret, pc_slide=True, fail_notice=False)
        xiaoding.send_markdown('Title', text=content, is_at_all=atAll)
        return {'status': 'ok', 'msg': '发送成功'}
    except ImportError:
        return {'status': 'error', 'msg': '请引入 dingtalkchatbot 模块'}
    except Exception as error:
        return {'status': 'error', 'msg': '发送失败' + str(error)}
    
    

if __name__ == "__main__":
    app.run(debug=False, port=5000, host='0.0.0.0')