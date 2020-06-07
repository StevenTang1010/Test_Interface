import pytest

from test_requests.api.base_api import BaseApi
from test_requests.api.tag import Tag


class TestTag:
    test_data = BaseApi.load('./tag_yaml/tag_data.yaml')
    # print(f'test_data is {test_data}')

    @classmethod
    def setup_class(cls):
        # pass
        cls.tag = Tag()
        # data = cls.tag.get_all()
        # # 遍历所有用例
        # for members in cls.test_data.values():
        #     # 遍历单个接口用例内的所有元素
        #     if members != []:
        #         for member in members:
        #             print(member)
        #             # 取到字典对象元素后遍历取值
        #             for name in member.values():
        #                 tag_id = cls.tag.json_path(data, f'$..tag[?(@.name=="{name}")].id')
        #                 if tag_id:
        #                     cls.tag.delete(tag_id[0])

    @pytest.mark.parametrize('member', test_data.get('get'))
    def test_get(self, tag_get, member):
        assert self.tag.get(tag_get, member)['errcode'] == 0

    @pytest.mark.parametrize('member', test_data.get('add'))
    def test_add(self, tag_add, member):
        assert self.tag.add(tag_add, member)['errcode'] == 0

    @pytest.mark.parametrize('member', test_data.get('update'))
    def test_update(self, tag_update, member):
        assert self.tag.update(tag_update, member)['errcode'] == 0

    @pytest.mark.parametrize('member', test_data.get('delete'))
    def test_delete(self, tag_delete, member):
        assert self.tag.delete(tag_delete, member)['errcode'] == 0
