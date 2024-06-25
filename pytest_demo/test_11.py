import pytest


def test_fun():
    n=1
    while True:
        print(f"这是我的第{n}次测试")
        n+=1
        if n==5:
            pytest.skip("当前我已经执行了5次测试，不再执行")