"""
使用前需要安装
pip install fake-useragent

"""
from fake_useragent import UserAgent

class RandUserAgent:
    def __init__(self):
        self.ua = UserAgent()

    def get_rand_ua(self):
        return self.ua.random


if __name__ == '__main__':
    o = RandUserAgent()
    res = o.get_rand_ua()
    print(res)