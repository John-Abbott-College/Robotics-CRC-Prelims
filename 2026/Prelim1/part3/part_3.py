# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 1.
Ceci est le fichier template pour la partie 3 du Prelim 1.
"""
def find_all(sentence:str, char:str) -> list[int]:
    return [i for i,s in enumerate(sentence) if s == char]



def part_3(sentence: str):
    """
    Find "ornithorynque" in the sentence

    Parameters:
        sentence str: The sentence that may contain contain the letters of "ornithorynque"

    Returns:
        [int]: The position of the letters found
    """
    WORD: str ="ornithorynque"
    positions = []

    for i,char in enumerate(WORD):
        idx = -1
        for index in find_all(sentence, char):
            if index not in positions:
                idx = index
                break
        positions.append(idx)

    return positions

print(part_3("Platypus is the best animal in the world."))