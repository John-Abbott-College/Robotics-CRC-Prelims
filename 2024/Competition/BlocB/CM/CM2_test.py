from CM2 import solve

def test_document1():
    assert(solve(35, 34) == 114)

def test_document2():
    assert(solve(23, 37) == 93)

def test_document3():
    assert(solve(0, 63) == 167)

def test_document4():
    assert(solve(50, 55) == 182)

