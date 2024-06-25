import pytest


@pytest.fixture(autouse="true")
def login():
    print("当 autouse为 Ture时")

class TestClass:
    def test_case1(self):
        print("test_case1")

    def test_case2(self):
        print("test_case2")

if __name__ == '__main__':
    pytest.main()