import random
from MM import solve

def test_master_mind():
    global master
    global win
    global tries
    tries = 0
    win = False
    master = [random.choice(['/', '#', '=', '+', '-', '*']) for _ in range(4)]
    solve(verif_function)
    assert(win)

def verif_function(guess):
    global tries
    global win
    if tries >= 20:
        assert(win)
    if win:
        return (4, 0)
    
    if master == guess:
        print('Victory!')
        win = True
        return (4, 0)
    perfect = 0
    almost = 0
    temp_list = master.copy()

    for i in range(len(master)):
        if guess[i] == temp_list[i]:
            perfect += 1
            temp_list[i] = None

        elif guess[i] in temp_list:
            almost += 1
            temp_list[temp_list.index(guess[i])] = None

    tries += 1
    return (perfect, almost)