


import allure
import pytest
@allure.title("allure test01")
def test_01():
    print("test 01")

@pytest.fixture()
@allure.title("allure pytest fixture")
def fixture_allure():
    print("fixture_allure")
    assert True
@allure.title("allure test02")
def test_02(fixture_allure):
    print("test 02")
    pass

@allure.title("allure test03")
def test_03():
    allure.dynamic.title("test 03")
    print("这是测试！")
    pass



if __name__ == '__main__':
    pytest.main()