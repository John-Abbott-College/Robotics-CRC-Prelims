from TP2 import solve

def test_document1():
    assert(solve('h sti optto okytk', 'wyi hscmeiins rpi?') == 'why is this competition so kryptik?')

def test_document2():
    assert(solve('l optto epormaind accetvamn u!', 'acmeiind rgamto el r s rietfn') == 'la competition de programmation de la crc est vraiment fun!')

def test_document3():
    assert(solve('ial iprmrei o hthr!', 'fnlyzpe eg sntta ad') == 'finally zipper merge is not that hard!')

    