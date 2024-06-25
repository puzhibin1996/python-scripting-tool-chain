import pytest


class Test_Class:
    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    @pytest.mark.parametrize("a,b", [(1, 2), (0, 3)])
    def test_a(self, a, b):
        print("test data: a=%d,b=%d" % (a, b))
        assert a + b == 3
