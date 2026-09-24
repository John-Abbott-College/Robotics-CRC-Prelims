# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 1.
Ceci est le fichier template pour la partie 4 du Prelim 1.
"""
def calc_dist(point1_3d, point2_3d):
    import math
    delta_x = point1_3d[0] - point2_3d[0]
    delta_y = point1_3d[1] - point2_3d[1]
    delta_z = point1_3d[2] - point2_3d[2]

    return math.sqrt(delta_x**2 + delta_y**2 + delta_z**2)
def part_4(positions: [(int, int, int)]):
    """
    Find the closest preys to the platypus

    Parameters:
        positions [(int, int, int)]: The position of the platypus and all the preys

    Returns:
        [int]: The ascending order of the preys' distance to the platypus
    """
    order = []
    ### You code goes here ###
    ### Votre code va ici ###
    platypus = positions[0]
    prays = positions[1:]

    distances_positions = [(calc_dist(platypus, pray),i) for i,pray in enumerate(prays, start=1)]
    distances_positions.sort()

    return [i for dist, i in distances_positions]

print(part_4([(0, 0, 0), (5, 6, 4), (9, 9, 2), (6, 2, 3), (3, 8, 4)]))