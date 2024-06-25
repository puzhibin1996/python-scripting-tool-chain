
import pytest

@pytest.fixture(params=[1,2,3,4,5,{'a':1,'b':2,'c':3},(2,3,4,5,6)],ids=['1','2','3','4','5','6','7'])
def demo(request):
    return request.param



def test_01(demo):
    print("{}".format(demo))
