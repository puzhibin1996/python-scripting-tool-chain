import pytest


@pytest.fixture
def login():
    print("登录")
    a="puzhibin"
    return a


@pytest.fixture
def logout():
    print("退出")

class TestLogin:
    #传入login fixture
    def test_001(self,login):
        print("test_001,传入login fixture")
        assert login=="puzhibin"

    def test_002(self,logout):
        print("test_002，传入logout fixture")

    def test_003(self,login,logout):
        print("test_003，传入login和logout fixture")

    def test_004(self):
        print("test_004，不传入fixture")

if __name__ == '__main__':
    pytest.main()