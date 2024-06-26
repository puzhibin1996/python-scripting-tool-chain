import pytest
import allure


@allure.parent_suite("test_case_1 tests for web interface")
@allure.suite("test_case_1 tests for web interface")
@allure.sub_suite("test_case_1 tests for web interface")
def test_case_1():
    print("test_case_1")
    with allure.step("step 1"):
        assert True


def test_case_2():
    allure.dynamic.parent_suite("test_case_2 tests for web interface")
    allure.dynamic.suite("test_case_2 tests for web interface")
    allure.dynamic.sub_suite("test_case_2 tests for web interface")
    print("test_case_2")


if __name__ == '__main__':
    pytest.main()
