# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 2.
Ceci est le fichier template pour la partie 1 du Prelim 2.
"""

def part_1(d: int, ladders: list[tuple[int, int]], snakes: list[tuple[int, int]]):
    """
    Find the minimum amount of steps to complet Snakes and ladders

    Parameters:
        d int: The maximum value you can move per turn
        ladders list[tuple[int, int]]: The start and end coordinates of the ladders
        snakes list[tuple[int, int]]: The start and end coordinates of the snakes

    Returns:
        int: The minimum amount of steps
    """
    steps = 0
    ### YOUR CODE GOES HERE ###


    Current_tile =  0 #The tile the player is at
    safe = True #To see whether a tile is safe or not
    roll = d #The roll performed

    while Current_tile != 100: #As long as they haven't reach the goal
       

        for i in snakes:
            if Current_tile + roll == i[1]: 
                safe = False
                roll -=1
                
        

            
        
        
        if safe == True: # if the roll is possible
            Current_tile += roll
            steps += 1
            #see the steps
            print("roll", str(roll))
            print("steps", str(steps))
            print("Tile", str(Current_tile))
            roll = d #resets the roll to max


        




            
        

    

    return steps


part_1(d = 6,
ladders = [(1, 38), (4, 14),(21, 42), (28, 84)],
snakes = [(48, 26), (49, 11), (62, 19), (87, 24)])
