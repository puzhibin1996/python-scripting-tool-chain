
import allure
import pytest


@allure.id("123")
def test_01():
    print("dayin - 123")

def test_02():
    print("dayin - 456")
    allure.dynamic.id("456")

if __name__ == '__main__':
    pytest.main()