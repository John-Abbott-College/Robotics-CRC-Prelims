# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 3.
Ceci est le fichier template pour la partie 5 du Prelim 3.
"""

def part_5(grid: [str]) -> str:
    """
    Find the actions to take from x to the $.

    Parameters:
        grid (str): The grid with all relevant positions and water drops

    Returns:
        str: A list of actions to take to get to the $
    """
    answer = ""
    ### You code goes here ###
    ### Votre code va ici ###
    


    return answer


# Uncomment the following print to test your function without pytest
# Décommenter la suite pour des tests sans pytest

grid1 = [' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 x 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 7 0 0',
' 0 0 3 0 0 0 0 0 0 0',
' 0 0 0 0 0 $ 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0']

grid2 = [' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 $ 0 0 0 0 0 5 0',
' 0 0 0 9 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 7 0 x',
' 0 0 0 0 5 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0']

grid3 = [' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 6 0 0 0 0',
' 0 5 0 0 0 0 0 0 $ 0',
' 0 0 0 3 0 0 0 0 0 0',
' 0 0 0 0 0 0 4 0 0 0',
' 0 x 0 0 0 0 0 0 0 0',
' 0 0 0 0 0 0 0 0 0 0',
' 0 0 0 0 8 0 0 0 0 0']

part_5(grid1)
part_5(grid2)
part_5(grid3)
