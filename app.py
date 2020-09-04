import sys
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')

config = {
    'name': '钉钉小助手',
    'robots': [{
        'name': '机器人',
        'key': 'k1',
        'access_token': '',
        'access_secret': '',
    }]
}

try:
    import local_setting
    config.update(local_setting.config)
except ImportError:
    pass

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

@app.route('/')
def index():
    return render_template('index.html', config=config)

@app.route('/execute', methods=["POST"])
def execute():
    params = parse_params(request)
    key = str(params['key'])
    content = str(params['content'])
    atAll = bool(params['atAll'])
    try:
        from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, FeedLink, CardItem
        xiaoding = DingtalkChatbot(new_webhook, secret=access_secret, pc_slide=True, fail_notice=False)
        return {'status': 'ok', 'msg': '发送成功'}
    except ImportError:
        return {'status': 'error', 'msg': '请引入 dingtalkchatbot 模块'}
    
    

if __name__ == "__main__":
    app.run(debug=False, port=5000, host='0.0.0.0')