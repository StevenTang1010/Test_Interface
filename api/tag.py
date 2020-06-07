from test_requests.api.base_api import BaseApi


class Tag(BaseApi):

    # 获取所有tag
    def get_all(self):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            'method': 'post',
            'params': {
                'access_token': self.token},
            'json': {
                'tag_id': []
            }}
        return self.send_api(data)

    # 获取指定tag
    def get(self, data, member):
        key = list(member.keys())[0]
        member[key] = self.json_path(self.get_all(), f'$..tag[?(@.name=="{member.get(key)}")].id')
        # print(member)
        raw = self.tamplate(data, member)
        return self.send_api(raw)

    # 添加tag
    def add(self, old_data, new_data):
        raw = self.tamplate(old_data, new_data)
        return self.send_api(raw)

    # 删除tag
    def delete(self, tag_delete, member):
        key = list(member.keys())[0]
        member[key] = self.json_path(self.get_all(), f'$..tag[?(@.name=="{member.get(key)}")].id')
        raw = self.tamplate(tag_delete, member)
        return self.send_api(raw)

    # 更新tag内容
    def update(self, tag_update, member):
        key = list(member.keys())[0]
        member[key] = self.json_path(self.get_all(), f'$..tag[?(@.name=="{member.get(key)}")].id')[0]
        raw = self.tamplate(tag_update, member)
        print(raw)
        return self.send_api(raw)
