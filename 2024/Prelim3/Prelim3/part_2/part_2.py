# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 3.
Ceci est le fichier template pour la partie 3 du Prelim 3.
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from part_1 import part_1
import math

def part_3(nbr_steps: int, row: str) -> [str]:
    """
    Find the drop and simulate propagation for n steps

    Parameters:
        nbr_steps (int): The number of steps for the simulation.
        row (str): The state of th row at the drop.

    Returns:
        [str]: the sequence of the expansion after a drop for n steps.
    """
    sequence = []
    ### You code goes here ###
    ### Votre code va ici ###



    return sequence



# Uncomment the following print to test your function without pytest (more tests using pytest)
# Décommenter la suite pour des tests sans pytest (il y a plus de tests avec pytest)

# print(part_3(3, ' 0 0 0 0 0 0 0 9 0 0'))