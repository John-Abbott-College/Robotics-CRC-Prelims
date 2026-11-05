from TP1 import solve

def test_document1():
    assert(solve('pour la compétItion de la cRc de ceTTe année voUs devez écrire en pYthon. Vous aLLez voir c’eST FAcile comme lanGage?') == 
           'Pour la compétition de la CRC de cette année vous devez écrire en python! Vous allez voir c’est Facile comme langage!')
    
def test_document2():
    assert(solve('FaUTe de GRAND-MÈRE.') == 'Faute de Grand-mère!')

def test_document3():
    assert(solve('cRc.') == 'CRC!')

def test_document4():
    assert(solve('TroP. De? pOINts! OUI Peut-ÊTRE.') == 'Trop! De! Points! Oui Peut-être!')
