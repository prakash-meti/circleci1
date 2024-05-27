def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def test_add():
    assert add(2, 7) == 9
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_sub():
    assert sub(5, 3) == 2
    assert sub(1, 1) == 0
    assert sub(-1, 1) == -2
    assert sub(3, 3) != 2
