from WW5 import solve

def test_document1():
    assert(solve(8.32, -12) == 491)

def test_document2():
    assert(solve(8.26, -12) == 431)

def test_document3():
    assert(solve(0.799, -11) == 163)
