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
    underscores= 2*size
    i = 0
    width = size
    while i < size+1:
        line = "|"
        j= 0
        while j  < width*2-1:
            line+="_."
            j+=1
        line+="_|"
        tail.append(line)
        i+=1 



    underscores=2*size-1
    print("Current progress:")
    for line in tail:
        print(line)    
    print("finished base, going to diagonal part")

    while i >= size+1 and i < 2*size+1:
        line = ""
        spaces = i-(size+1)
        for c in range(0,spaces+1):
            line+= " "

        line+="\\" 
        underscores-=1
        for p in range(0, underscores):
            line+= "_."
           

        line+="_/"

        for c in range(0,spaces+1):
            line+= " "
        
        
        tail.append(line)
        i+=1

    print_tail(tail)
        

    
    return tail



part_1(20)