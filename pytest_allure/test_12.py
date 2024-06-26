import allure

import pytest



@allure.step("Step 1")
def step1():
    print("step1")

@allure.step("Step 2 (with value {val})")
def step2(val):
    print("step2",val)

def test_case1():
    step1()
    for var in ["val1", "val2", "val3"]:
        step2(var)
def test_case2():
    with allure.step("Step 1"):
        print("我在test_case2中——step1")
    for var in ["val1", "val2", "val3"]:
        with allure.step("Step 2 (with value {val})".format(val=var)):
            print("我在test_case2中——step2",var)

if __name__ == '__main__':
    pytest.main()