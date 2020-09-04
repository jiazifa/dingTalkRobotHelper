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

