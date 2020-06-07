from pprint import pprint

import yaml

from test_requests.api.base_api import BaseApi


def test_load():
    with open('test_tagdata.yaml', 'r') as f:
        pprint(yaml.safe_load(f))
        # return yaml.safe_load(f)


def test_tamplate():
    print(BaseApi.tamplate('../api/tag_headers.yaml', {'token': "123", "name": 'demo'}))
