from DS3 import solve

def test_document1():
        tree = [['h'], 
        ['d', 'l'],
        ['b', 'f', 'j', 'n'],
        ['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o']]
    
        expected = 'abcdefghijklmno'
        assert(solve(tree) == expected)

def test_document2():
        tree = [['t'],
        ['R', 's'],
        ['C', 'C', 'e', 't']]
    
        expected = 'CRCtest'
        assert(solve(tree) == expected)

def test_document3():
        tree = [['t'],
        [' ', 'b'],
        ['R', 's', 'e', 's'],
        ['C', 'C', 'i', ' ', 'h', ' ', 'e', 't']]
        expected = 'CRC is the best'
        assert(solve(tree) == expected)
