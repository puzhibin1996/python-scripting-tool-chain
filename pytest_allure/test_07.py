import allure
import pytest

from allure_commons.types import LabelType

@allure.label(LabelType.LANGUAGE, "python")
@allure.label(LabelType.FRAMEWORK, "pytest")
def test_01():
    print("test_01")
    with allure.step("step 1"):
        assert True

def test_02():
    allure.dynamic.label(LabelType.LANGUAGE, "python")
    allure.dynamic.label(LabelType.FRAMEWORK, "pytest")
    print("test_02")

if __name__ == '__main__':
    pytest.main()