from TP3 import solve

def test_document1():
    assert(solve('laval') == 1)

def test_document2():
    assert(solve('cook') == 0)

def test_document3():
    assert(solve('wwwwwwwww') == 3)

def test_document4():
    assert(solve('oborobo') == 2)

    