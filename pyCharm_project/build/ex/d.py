# coding:utf-8
import ddt
import unittest
d12 =[{"username": "上海-悠悠", "psw": u"zhangxxx", "expect": True},{"username": "123", "psw": "xxx", "expect": False}]
@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data({"username": u"11", "psw": u"22", "expect": True}, {"username": "1", "psw": "2", "expect": False})
    def test_01(self, testdata):
        print(testdata)
    @ddt.data(*d12)
    def test_02(self, testdata):
        print(testdata)

if __name__ == "__main__":
    unittest.main()

