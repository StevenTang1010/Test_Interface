from jsonpath import jsonpath

from test_requests.api.user import User


class TestTag:
    def setup(self):
        self.user = User()

    def test_add(self):
        print(self.user.add(name='test3'))

    def test_get(self):
        # tags = json.dumps(self.tag.get(), indent=2)
        tag_id = jsonpath(self.user.get(), '$..tag[?(@.name=="")].id')
        if tag_id:
            self.user.delete(tag_id[0])

    def test_delete(self):
        pass
        # self.user.delete(tag_id='')

    def test_update(self):
        pass
        # self.user.update(tag_id='', tag_name='')
