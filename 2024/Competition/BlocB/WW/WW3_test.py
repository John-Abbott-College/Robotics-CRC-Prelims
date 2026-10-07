from WW3 import solve


def test_document1():
    assert(solve(6, 7, 8, 8.5, 9, 10, 0.5, 3) == 6)

def test_document2():
    assert(solve(40, 16, 8, 10, 200, 80, 1, 8) == 160)

def test_document3():
    assert(solve(33, 66, 0.9, 17, 666, 50, 3, 1000) == 0)

def test_document4():
    assert(solve(24, 90, 18, 1, 10, 60, 0.2, 3090) == 58710)

    