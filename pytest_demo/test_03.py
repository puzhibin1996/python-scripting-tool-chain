import pytest

# fixture作用于 scope=‘class’
@pytest.fixture(scope='class')
def login():
    print("scope为class")


class TestClass:
    def test_01(self, login):
        print("test_01")

    def test_02(self, login):
        print("test_02")

    def test_03(self, login):
        print("test_03")

if __name__ == '__main__':
    pytest.main()