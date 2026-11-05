from SC3 import solve

def test_document1():
    assert(solve(9) == [50,24])

def test_document2():
    assert(solve(37) == [722])

def test_document3():
    assert(solve(179) == [16200])

def test_document4():
    assert(solve(4279) == [9159200,836550,80000,28008])

def test_document5():
    assert(solve(888) == [198025,99458,66603,50176,33750,25538,22801,17328,13225,11858, 9126,6400,6253,5043,3698,3626,2775,2401,2368,1998,1850,1813])
