import pytest

@pytest.fixture(autouse=True)
def login():
    print("登录")

def test_01():
    print("测试用例01")

@pytest.mark.skip(reason="单个不执行")
def test_02():
    print("测试用例02")



class TestClass:
    def test_case1(self):
        print("TestClass-测试用例01")

    @pytest.mark.skip(reason="这个类里面的不执行")
    def test_case2(self):
        print("TestClass-测试用例02")


@pytest.mark.skip(reason="整个类不执行")
class TestClass2:
    def test_case01(self):
        print("TestClass2-测试用例01")