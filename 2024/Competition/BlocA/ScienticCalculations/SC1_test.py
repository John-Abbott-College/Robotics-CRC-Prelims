from SC1 import solve

def test_booklet():
    assert(abs(solve(2, 5, 10000) - 0.502654825) < 0.05)
    assert(abs(solve(3, 4, 100000) - 1.0) < 0.0000000005)
    assert(abs(solve(2, 4, 10000) - 0.7853981633974483) < 0.05)

def test_other():
    assert(abs(solve(6, 12, 10000) - 0.7853981633974483) < 0.05)

def test_other2():
    assert(abs(solve(4, 12, 100000) - 0.3490658503988659) < 0.05)

