import sys

import pytest

if sys.platform.startswith('win'):
    pytest.skip("skipping windows-only tests",allow_module_level=True)


@pytest.fixture(autouse=True)
def login():
    print("login")

def test_1():
    print("test_1")