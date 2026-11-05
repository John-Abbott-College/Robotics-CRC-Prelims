from WW2 import solve

def test_document1():
    assert(solve([['rose', '8'],
['tulip', '6'],
['petunia', '4'],
['sunflower', '5'],
['orchid', '4'],
['lily', '11'],
['iris', '8']]
) ==
['', 'lily', '', '', 'iris rose', '', 'tulip', 'sunflower', 'orchid petunia', '', '', ''])
 
def test_document2():
    assert(solve([['sunflower', '5'],
['petunia', '4'],
['lily', '11'],
['geranium', '7'],
['daffodil', '12'],
['lavender', '2']]
) ==
['daffodil', 'lily', '', '', '', 'geranium', '', 'sunflower', 'petunia', '', 'lavender', ''])
 
def test_document3():
    assert(solve([['lily', '11'],
['geranium', '7'],
['daffodil', '12'],
['iris', '8'],
['lavender', '2']]
) ==
['daffodil', 'lily', '', '', 'iris', 'geranium', '', '', '', '', 'lavender', ''])
 
