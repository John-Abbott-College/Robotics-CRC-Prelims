# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 1.
Ceci est le fichier template pour la partie 2 du Prelim 1.
"""

def part_2(w: int, h: int, l: int, a: int):
    """
    Finds the amount of milk produced by the platypus

    Parameters:
        w int: The width of the platypus
        h int: The height of the platypus
        l int: The length of the platypus
        a int: The age of the platypus

    Returns:
        float: The amount of milk produced with 2 decimal precision
    """
    milk = 0.0
    ### You code goes here ###
    ### Votre code va ici ###

    A = w/2 #half the width of the platypus
    b= l/2 #half the length of the platypus
    c= h/2 #half the height of the platypus
    
    #The calculated volume
    milk =round((((4/3)*3.141592)*A*b*c)/2*(a*0.1), 2)
    print(str(milk))
    return milk

part_2(w = 10, h = 14, l = 50, a = 4)