

import allure
import pytest


def test_01():
    allure.dynamic.tag("new123","puzhibin","666")
    print("test_01")

@allure.tag("new456","zengting","666")
def test_02():
    print("test_02")


if __name__ == '__main__':
    pytest.main()