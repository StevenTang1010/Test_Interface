import pytest
import yaml


# global test_data


@pytest.fixture(scope='class', autouse=True)
def get_tag_headers() -> dict:
    # global test_data
    with open('./tag_yaml/tag_headers.yaml', 'r', encoding='utf8') as f:
        headers = yaml.safe_load(f)
    # with open('./test_tag/tag_yaml/tag_data.yaml', 'r', encoding='utf8') as f:
    #     test_data = yaml.safe_load(f)
    return headers


@pytest.fixture()
def tag_get(get_tag_headers):
    # print(get_tag_headers.get('get'))
    return get_tag_headers.get('get')


@pytest.fixture()
def tag_add(get_tag_headers):
    return get_tag_headers.get('add')


@pytest.fixture()
def tag_update(get_tag_headers):
    return get_tag_headers.get('update')


@pytest.fixture()
def tag_delete(get_tag_headers):
    return get_tag_headers.get('delete')
