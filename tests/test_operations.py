from src.math_operations import add, subtract

def test_add():
    assert add(1,2) == 3
    assert add(-1,11) == 0


def test_subtract():
    assert subtract(5,1) == 4
    assert subtract(4,3) == 1
    assert subtract(3,3) == 0
    assert subtract(2,3) == 1
    