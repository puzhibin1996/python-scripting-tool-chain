import os
import sys
import time
import pytest

base_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

sys.path.append(base_path)

class TestApi:
    def test_01(self):
        print("Running test_01")
    def test_02(self):
        print("Running test_02")




