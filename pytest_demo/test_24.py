
import pytest

@pytest.mark.flaky(reruns=5)
def test_example():
    import random
    assert random.choice([True,False,False])

@pytest.mark.flaky(reruns=5,reruns_delay=1)
def test_example():
    import random
    assert random.choice([True,False,False])


if __name__ == '__main__':
    pytest.main()