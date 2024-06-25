import pytest

pexpect = pytest.importorskip("pexpect",minversion="4.2")


@pexpect
def test_imp():
    print("test")