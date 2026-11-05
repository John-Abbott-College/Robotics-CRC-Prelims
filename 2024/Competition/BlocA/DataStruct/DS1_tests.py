from DS1 import solve

def test_document1():
    assert(solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

def test_document2():
    assert(solve([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]])


def test_document3():
    assert(solve([[12, 46, 213, 4123]]) == [[12], [46], [213], [4123]])

def test_document4():
    assert(solve([['ah', 'bé', 'cé', 'dé'], ['euh', 'èf', 'jé', 'ache']]) == [['ah', 'euh'], ['bé', 'èf'], ['cé', 'jé'], ['dé', 'ache']])


