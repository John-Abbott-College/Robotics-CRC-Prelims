# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 1.
Ceci est le fichier template pour la partie 1 du Prelim 1.
"""

# just a small helper to visualize the tail
def print_tail(tail: [str]):
    for line in tail:
        print(line)

def top(n:int)->list[str]:
    lines = []
    width = 2*n
    for _ in range(n+1):
        line = "|"
        line += (width -1)*"_."
        line += "_|"
        lines.append(line)
    
    return lines

def bottom(n:int)->list[str]:
    lines =[]
    max_width = 2 * n -1
    min_width = max_width - n
    
    space =" "
    for width in range(max_width, min_width, -1):
        line = f"{space}\\"
        line += (width-1)*"_."
        line += f"_/{space}"
        lines.append(line)
        space += " "
        
    return lines
    
    
def part_1(size: int):
    """
    Draw the platypus tail

    Parameters:
        size int: Size of the tail

    Returns:
        [String]: The platypus tail drawn
    """
    tail = []
    ### YOUR CODE GOES HERE ###
    tail += top(size)
    tail += bottom(size)
    return tail

val = part_1(7)
print("\n".join(val))