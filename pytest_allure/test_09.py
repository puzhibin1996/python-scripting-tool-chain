import pytest
import allure

@allure.link("https://www.baidu.com",name="百度")
@allure.issue("AUTH-123")
@allure.testcase("puzhibin-testcase")
def test_case01():
    print("test_case01")


def pr(pr_id):
    return allure.link(pr_id,name="PR{}".format(pr_id),link_type="pr")

@pr(123)
def test_case02():
    pr("test_case02")

def test_case03():
    allure.dynamic.link("https://www.baidu.com",name="百度")
    allure.dynamic.issue("AUTH-123")
    allure.dynamic.testcase("puzhibin-testcase")


if __name__ == '__main__':
    pytest.main()

