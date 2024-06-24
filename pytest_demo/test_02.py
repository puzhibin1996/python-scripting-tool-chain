import pytest


# fixtrue作为参数，互相调用传入
@pytest.fixture
def account():
    a="account"
    print("第一层fixture")
    return a

#Fixture的相互调用一定是要在测试类里调用这层fixture才会生次，普通函数单独调用是不生效的
@pytest.fixture
def login(account):
    print("第二层fixture")

class TestClass:
    def test_1(self,login):
        print("直接使用第二层fixture，返回值为{}".format(login))
    def test_2(self,account):
        print("直接使用第一层fixture，返回值为{}".format(account))

if __name__ == '__main__':
    pytest.main()