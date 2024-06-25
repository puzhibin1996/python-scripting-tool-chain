import pytest


class Test_ABC:

    def setup_calss(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def test_1(self):
        print("test_1")
        assert 1

    @pytest.mark.skipif(condition=2>1,reason="跳过该函数")
    def test_2(self):
        print("test_2")
        assert 0

