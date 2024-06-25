import sys

import pytest
# 标记
skipmark = pytest.mark.skip(reason="不能再windows上面运行")
skipifmark = pytest.mark.skipif(sys.platform=="win32",reason="不能在windows上面运行")


@skipmark
class TestSkip_Mark(object):
    @skipifmark
    def test_fun(self):
        print("测试标记")

    def test_pzb(self):
        print("测试标记")


@skipmark
def test_skip():
    print("测试标记")