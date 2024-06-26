from os.path import basename,expanduser

import allure
import pytest

@pytest.mark.parametrize("login",["johndoe","2222@qq.com"])
def test_authetication(login):
    with allure.step("步骤1：打开百度首页"):
        print("步骤1：打开百度首页")
    with allure.step("步骤2：输入用户名{}".format(login)):
        print("步骤2：输入用户名{}".format(login))
    with allure.step("步骤3：点击登录"):
        print("步骤3：点击登录")
    with allure.step("步骤4：校验登录成功"):
        print("步骤4：校验登录成功")

def test_authentication_with_empty_login():
    allure.dynamic.parameter("login","(empty)")
    print("test_authentication_with_empty_login")

@pytest.mark.parametrize("ssh_key",[
    expanduser("~/.ssh/id_rsa1"),
    expanduser("~/.ssh/id_rsa2"),
    expanduser("~/.ssh/id_rsa3"),
])
def test_authentication_with_ssh_key(ssh_key):
    allure.dynamic.parameter("ssh_key",basename(ssh_key))
    print("test_authentication_with_ssh_key")


if __name__ == '__main__':
    pytest.main()
