import pytest


class Test_class:
    def setup_class(self):
        print("setup_class called")
    def teardown_class(self):
        print("teardown_class called")

    def test_1(self):
        print("test_1")
        assert 1
    @pytest.mark.xfail(2>1,reason="标注为预期失败")
    def test_2(self):
        print("test_2")
        assert 0