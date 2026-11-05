from WW4 import solve

def test_document1():
    assert(solve(10, 5) == 29)

def test_document2():
    assert(solve(20, 10) == 64)

def test_document3():
    assert(solve(11, 7) == 37)
