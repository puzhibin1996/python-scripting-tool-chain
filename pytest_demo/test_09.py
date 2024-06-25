
import pytest

@pytest.fixture(name='new_fixture')
def test_name():
    print("test_name")
    pass

def test_01(new_fixture):
    print("使用name参数后，传入重命名函数，执行成功")

def test_02(test_name):
    print("使用name参数后，仍传入函数名称，会失败")