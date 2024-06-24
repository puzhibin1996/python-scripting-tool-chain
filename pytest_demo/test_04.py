import pytest


@pytest.fixture(scope="class")
def login():
    a='123'
    print("输入zhanghao")

class TestLogin:
    def test_01(self):
        print("test_01")

    def test_02(self,login):
        print("test_02")

    def test_03(self,login):
        print("test_03")

    def test_04(self):
        print("test_04")

if __name__ == '__main__':
    pytest.main()