import pytest


@pytest.fixture(scope="module")

def login():
    print("fixture范围 为 module")

def test_01():
    print("test_01")

def test_02(login):
    print("test_02")


class TestClass:
    def test_001(self):
        print("test_001")

    def test_002(self):
        print("test_002")

    def test_003(self):
        print("test_003")

if __name__ == '__main__':
    pytest.main()