

import pytest

@pytest.mark.model
def test_model_a():
    print("test_model_a")

@pytest.mark.regular
def test_regular_a():
    print("test_regular_a")

@pytest.mark.model
def test_model_b():
    print("test_model_b")

@pytest.mark.regular
def test_regular_b():
    print("test_regular_b")


def testnoMark():
    print("testnoMark")




