from CM1 import solve

def test_document1():
    verif(solve(4), 4)

def test_document2():
    verif(solve(8), 8)


def test_document3():
    verif(solve(9), 9)



def verif(queens, n):
    row = [0 for _ in range(n)]
    col = [0 for _ in range(n)]
    d1 = [0 for _ in range(2*n - 1)]
    d2 = [0 for _ in range(2*n - 1)]

    for queen in queens:
        row[queen[0]] += 1
        col[queen[1]] += 1
        d1[queen[0] + queen[1]] += 1
        d2[n - queen[0] + queen[1]] += 1
    
    assert(row == [1 for _ in range(n)])
    assert(col == [1 for _ in range(n)])
    for el in d1:
        if el > 1:
            assert(False)
    for el in d2:
        if el > 1:
            assert(False)


