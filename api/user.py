from test_requests.api.base_api import BaseApi
from test_requests.api.wework import WeWork


class User(BaseApi):

    def __init__(self):
        self.token = WeWork().get_token().get('access_token')
        print(self.token)

    # 新增成员
    def add(self, userid, name):
        data = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/user/create',
            'method': 'post',
            'params': {
                'access_token': self.token
            },
            'json': {
                "userid": userid,
                "name": name,
            }
        }
        return self.send_api(data)

    # 获取成员
    def get(self):
        data = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/user/get',
            'method': 'post',
            'params': {
                'access_token': self.token
            },
        }
        return self.send_api(data)

    # 删除成员
    def delete(self, userid):
        data = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            'method': 'post',
            'params': {
                'access_token': self.token
            },
            'json': {
                "userid": userid,
            }
        }
        return self.send_api(data)

    # 更新成员
    def update(self, user_dict: dict):
        data = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/user/update',
            'method': 'post',
            'params': {
                'access_token': self.token
            },
            'json': user_dict
        }
        return self.send_api(data)

    # 批量删除
    def batchdelete(self, useridlist: list):
        data = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete',
            'method': 'post',
            'params': {
                'access_token': self.token
            },
            'json': {
                "useridlist": useridlist
            }
        }
        return self.send_api(data)

    # 获取部门成员
    def simplelist(self, department_id):
        data = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist',
            'method': 'post',
            'params': {
                'access_token': self.token
            },
            'json': {
                "department_id": department_id
            }
        }
        return self.send_api(data)
