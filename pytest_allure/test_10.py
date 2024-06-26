import pytest
import allure


@allure.epic("web interface")
@allure.feature("essential features")
@allure.story("authentication")
def test_case01():
    print("test_case01")

def test_case02():
    allure.dynamic.epic("ahh iiii")
    allure.dynamic.feature("hhhhh hhhh ")
    allure.dynamic.story("hhhh hhh hh ")
    print("test_case02")

if __name__ == '__main__':
    pytest.main()