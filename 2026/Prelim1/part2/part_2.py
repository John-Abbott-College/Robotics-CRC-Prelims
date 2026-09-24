# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 1.
Ceci est le fichier template pour la partie 2 du Prelim 1.
"""
import math
def volume(a:int, b:int, c:int):
    return (4/3)*math.pi*a*b*c
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
    increase = 0.1 * a
    milk = (0.5)*volume(w/2,h/2,l/2)*increase


    return round(milk,2)

print(part_2(w = 10, h = 14, l = 50, a = 4))