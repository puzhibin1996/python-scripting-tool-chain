import pytest


def return_test_data():
    return[(1,322),(5450,3)]

class TestClass:
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")

    @pytest.mark.parametrize("a,b",return_test_data())
    def test_1(self,a,b):
        print("test data : a=%d,b=%d"%(a,b))
        assert a+b>=2