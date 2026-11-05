# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 3.
Ceci est le fichier template pour la partie 2 du Prelim 3.
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from part_1 import part_1

def part_2(nbr_steps: int, grid: [str]) -> [[str]]:
    """
    This simulates a drop of water on a calm surface.

    Parameters:
        nbr_steps (int): The number of steps of the simulation you need to run
        grid ([str]): The grid containing the drop point and strength

    Returns:
        [[str]]: The grids with the wave for the number of steps specified
    """
    results = []
    ### You code goes here ###
    ### Votre code va ici ###



    return results

# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest

#print(part_2(2,[' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 9 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0', ' 0 0 0 0 0 0 0 0 0 0'])) # Expected: '8111'



