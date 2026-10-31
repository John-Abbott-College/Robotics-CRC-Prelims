from twoD4 import solve

def test_document1():
    assert(solve('01010100', '10101011') == [
"  x   x  ",
"         ",
"x x x x  ",
"         ",
"  x o x  ",
"         ",
"    x x  ",
"         ",
"      x  "])
    

def test_document2():
    assert(solve('01010101', '11001010') == 
[" x x ",
 "xxxxx",
 " xox ",
 "xxxxx",
 " x x "])
    
def test_document3():
    assert(solve('10001000', '10111011') == 
["xxx  ",
 " xxx ",
 "  xxx",
 "xxx  ",
 " xox ",
 "  xxx",
 "xxx  ",
 " xxx ",
 "  xxx"]
)
    
def test_document4():
    assert(solve('00100101', '01101101') == 
["     xx                        ",
 "      xxxx                     ",
 "     xxxx xx                   ",
 "      xxxxxxx                  ",
 "     xxxxxxxxxxxx              ",
 "      xxxxxxxxxxxxx            ",
 "     xx  xxxxxxxxxxxxx         ",
 "      xxxxxxxxxxxxxxxxxx       ",
 "     xxxxxxxxxxxxxxxxxxxxx     ",
 "      xxxxxxxxxxxxxxxxxxx xx   ",
 "     xxxxxxx  xoxxxxxxxxxxxxxxx",
 "      xxxxxxxxxxxxxxxxxxx xx   ",
 "     xxxxxxxxxxxxxxxxxxxxx     ",
 "      xxxxxxxxxxxxxxxxxx       ",
 "     xx  xxxxxxxxxxxxx         ",
 "      xxxxxxxxxxxxx            ",
 "     xxxxxxxxxxxx              ",
 "        xxxxxxx                ",
 "     xxxx xx                   ",
 "      xxxx                     ",
 "     xx                        "])
    