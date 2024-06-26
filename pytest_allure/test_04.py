import allure
import pytest




@allure.description("我是测试01")
def test_01():
    print("打印-我是测试01")



def test_02():
    allure.dynamic.description("我是测试02")
    print("打印-我是测试02")


if __name__ == '__main__':
    pytest.main()