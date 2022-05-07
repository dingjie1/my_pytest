import requests
from conftest import *

class Request:
    # 通用http_request接口工具（POST|GET|PUT）
    _timeout = 6

    @classmethod
    def http_request(cls, url, method, data):
        result = None
        if method == 'POST':
            try:
                response = crm.request.post(url=url, data=json.dumps(data), timeout=cls._timeout)
                result = response.json()
            except BaseException as e:
                print(f"post_error:{e}")
        elif method == 'GET':
            try:
                response = crm.request.get(url=url, params=data, timeout=cls._timeout)
                result = response.json()
            except BaseException as e:
                print(f"get_error:{e}")
        elif method == 'PUT':
            try:
                response = crm.request.put(url=url, data=json.dumps(data), timeout=cls._timeout)
                result = response.json()
            except BaseException as e:
                print(f"post_error:{e}")
        else:
            print(f"method_error")
        return result
