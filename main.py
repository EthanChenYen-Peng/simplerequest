# encoding=utf-8
import json
import sys
import simplehttp
from simplehttp.error import HttpError
import pdb


def case2():
    url_target = "https://httpbin.org/get?debug=true"
    params = {"name": u"常⾒見見問題 q&a"}
    r = simplehttp.get_json(url_target, params)
    print(simplehttp)
    assert r['args'] == {'debug': 'true', 'name': u'常⾒見見問題 q&a'}


def case3():
    url_target = "https://httpbin.org/post"
    data = {"isbn": "9789863479116", "title": u"流暢的 Python"}
    params = {"debug": "true"}
    r = simplehttp.post_json(url_target, params, data)
    # print type(r['json'])
    assert r['args'] == {'debug': 'true'}


def errorCode():
    try:
        pdb.set_trace()
        r = simplehttp.post_json("https://httpbin.org/status/400")
    except HttpError as e:
        print(e)
        print(e.message)


def noneValidJson():
    url_target = "https://google.com/"
    r = simplehttp.get_json(url_target)


def connectionError():
    # url_target = "dummy"
    url_target = "hs://httpbin.org"
    pdb.set_trace()
    try:
        r = simplehttp.get_json(url_target)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    # noneValidJson()
    # errorCode()
    connectionError()
