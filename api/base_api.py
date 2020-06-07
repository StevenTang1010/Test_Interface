from pprint import pprint
from string import Template

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:
    # 获取token
    def __init__(self):
        self.token = self._get_token().get('access_token')
        # print(self.token)

    # 发送请求接口
    def send_api(self, req: dict):
        # 使用 requests 完成多请求的改造
        # pprint(req)
        r = requests.request(**req)
        pprint(r.json())
        return r.json()

    def _get_token(self):
        id = 'ww88a5b90ab85e3f31'
        secret = 'jW2E8jzeMeY9HHf-Aa6wLPhIPvQrqq9MKDOv9oXt380'
        data = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={secret}',
            'method': 'get'
        }
        return self.send_api(data)

    # json内容提取器，传入jsonpath表达式
    @classmethod
    def json_path(cls, json, expr):
        return jsonpath(json, expr)

    # 加载yaml文件内容
    @classmethod
    def load(cls, path):
        with open(path, 'r', encoding='utf8') as f: data = yaml.safe_load(f)
        return data

    # 对需要修改的参数做修改
    def tamplate(self, old_data, new_data=None, sub=None):
        # with open(old_data, 'r') as f:
        #     yaml_data = yaml.safe_load(f)
        # for key in new_data.keys():
        #     if key in old_data:
        # old_data[key] = new_data.get(key)
        # if sub is None:
        #     return yaml.load(Template(
        #             yaml.dump(
        #                 yaml.safe_load(f))).substitute(data))
        # else:
        data = {'token': self.token}
        if new_data:
            data.update(new_data)
        return yaml.load(Template(yaml.dump(old_data)).substitute(data))