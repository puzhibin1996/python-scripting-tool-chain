import pytest


class Test_class:
    def setup_class(self):
        print("setup_class called")

    def teardown_class(self):
        print("teardown_class called")

    @pytest.mark.parametrize("a", [3, 6])
    def test_a(self, a):
        print("test data:a=%d"%a)
        assert a % 3 == 0
