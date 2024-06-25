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

if __name__ == '__main__':
    pytest.main(['--alluredir', './pytest_allure/allure-results/temps'])
    time.sleep(2)
    os.system("allure generate ./pytest_allure/allure-results/temps -o ./pytest_allure/allure-results/report --clean")
    os.system("allure open ./pytest_allure/allure-results/report")
