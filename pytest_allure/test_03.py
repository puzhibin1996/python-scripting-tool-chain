import allure
import pytest

@pytest.mark.parametrize("login",["puzhibin","1075057376@qq.com"])
@allure.title("这是是Login (as{login})")
def test_login1(login):
    print(login)


@pytest.mark.parametrize("login1",["zengting","1075057376@qq.com"],ids=["using-username","using-email"])
@allure.title("这是Login ({param_id})")
def test_login2(login1):
    print(login1)



if __name__ == '__main__':
    pytest.main()