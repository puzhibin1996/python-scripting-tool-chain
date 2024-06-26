import allure
import pytest


from allure_commons.types import Severity


@allure.severity(Severity.CRITICAL)
def test_01():
    print("test_01")

@allure.severity(Severity.TRIVIAL)
def test_02():
    print("test_02")

@allure.severity(Severity.BLOCKER)
def test_03():
    print("test_03")


def test_04():
    allure.dynamic.severity(Severity.MINOR)
    print("test_04")

def test_05():
    allure.dynamic.severity(Severity.NORMAL)
    print("test_05")


if __name__ == '__main__':
    pytest.main()