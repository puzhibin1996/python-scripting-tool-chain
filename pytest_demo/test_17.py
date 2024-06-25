import pytest


@pytest.mark.parametrize("test_input , expected",[("3+5",8),("2+4",6),("6*9",42)])
def test_eval(test_input, expected):
    print(f"测试数据{test_input},期望结果{expected}")
    assert eval(test_input) == expected