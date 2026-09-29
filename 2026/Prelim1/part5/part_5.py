# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 1.
Ceci est le fichier template pour la partie 5 du Prelim 1.
"""

def part_5(turns: int, board: [str]):
    """
    Simulate the Game of platypus

    Parameters:
        turns str: The number of turns in the game
        board [str]: The 16x16 grid representing the board of the Game of platypus with x as the platypus and . the food

    Returns:
        str: Is the platypus surviving ("Yes" or "No")
    """
    final_answer = "No"
    ### You code goes here ###
    ### Votre code va ici ###

    
    xp : int
    yp : int
    platypusCoordinates= ()
    foodcoordinates= []
    dotlocation = ()
    for yp, line in enumerate(board):
        # = board.index(line)
        print("yp: ",yp)
        for xp, c in enumerate(line):
            if c == 'x':                 
                    print("Xp: ",xp)
                    platypusCoordinates= (xp,yp)
                    break
            else:
                print("no platypus at: ",c)
    print(platypusCoordinates)

    for y2, line in enumerate(board):
         print("y2", y2)
         for x2, c in enumerate(line):
              if c== '.':
                   print("found food at x: ",x2)
                   dotlocation = (x2, y2)
                   foodcoordinates.append(dotlocation)
    print(foodcoordinates)
    return final_answer

    


part_5(turns = 11, 
        board = [
            "___x_.________._",
            "_______.________",
            "_________..___._",
            "_.__._____.____.",
            "_________.__.___",
            ".____________._.",
            "_.__________.___",
            "__.______..__.__",
            "____._______.___",
            ".__.___.________",
            "______._________",
            "____..._____.___",
            "__..___.._______",
            "_______________.",
            "________._._____",
            "____.._______.__",
        ])