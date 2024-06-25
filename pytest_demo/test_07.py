import pytest


@pytest.fixture(params=[1,2,{'a':1,'b':2},(4,5,6)])
def demo(request):
    return request.param


def test_demo(demo):
    print("值{}".format(demo))