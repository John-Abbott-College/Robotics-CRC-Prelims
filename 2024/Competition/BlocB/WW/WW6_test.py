from WW6 import solve

def test_document1():
    assert(solve(40, 0.05, 30, 2) == [32.684, 37.799])

def test_document2():
    assert(solve(80, 0.01, 15, 2) == [18.285, 24.703])

def test_document3():
    assert(solve(30, 0.05, 45, 4) == [24.775, 36.237])
