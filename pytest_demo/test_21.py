import pytest

data1=[1,2,3]
data2=['a','b']


@pytest.mark.parametrize('a',data1)
@pytest.mark.parametrize('b',data2)
def test_case(a,b):
    print(f"笛卡尔积，测试数据为：{a},{b}")
