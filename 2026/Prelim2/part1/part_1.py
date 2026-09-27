# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 2.
Ceci est le fichier template pour la partie 1 du Prelim 2.

"""
def find_next_best_ladder(ladders:list[tuple[int,int]])->tuple[int,int]:
    """
    Finds the ladder giving the largest jump from a list of ladders
    """
    dist_ladders = [(l[1]-l[0], l) for l in ladders if l[0]]
    dist_ladders.sort(reverse=True)
    return dist_ladders[0][1]

def find_path(ladders:list[tuple[int,int]]) -> list[tuple[int,int]]:
    """
    This function selects the best combination of ladders starting from the end
    of the maze (100) until there are no more possible ladders.
    """
    best_ladders= []
    # All ladders are possible ones at the start
    possible_ladders = ladders.copy() #making a deep copy to avoid modifying the original list

    #Starting from the end of the board
    position = 100

    while possible_ladders:
        print("Searching for next best ladder to take")
        next_best = find_next_best_ladder(possible_ladders)
        best_ladders.append(next_best)

        # restart the search from the base of the selected ladder
        # keep only the ladders that come before this one
        position = next_best[0]
        possible_ladders = [l for l in possible_ladders if l!= next_best and l[1] <= position]

    # since we started from the end of the snake board, we have to provide the ladder
    # in the order they'll actually be encountered
    best_ladders.reverse()

    return best_ladders

def count_throws(start:int, stop:int, d:int, snakes:list[tuple[int,int]])->int:
    """
    This function finds a combination of dice throws from 1-d, to go from start to end
    while avoiding snakes heads.
    """
    if start >= stop:
        print("This isn't possible")
        return -1

    # searching for all the snake heads to avoid them
    heads  = [head for head,_ in snakes]
    count = 0

    #Searching for the path with the least throws
    current = start
    while current != stop:
        for step in range(d, 0, -1):
            if (current + step) not in heads and (current +step) <= stop:
                print(f"Dice: {step} -> Going from:{current} to {current+step}")
                current += step
                count += 1
                break

    return count

def part_1(d: int, ladders: list[tuple[int, int]], snakes: list[tuple[int, int]]):
    """
    Find the minimum amount of steps to complete Snakes and ladders

    Parameters:
        d int: The maximum value you can move per turn
        ladders list[tuple[int, int]]: The start and end coordinates of the ladders
        snakes list[tuple[int, int]]: The start and end coordinates of the snakes

    Returns:
        int: The minimum amount of steps
    """
    steps = 0
    ### YOUR CODE GOES HERE ###
    path = find_path(ladders)
    position = 0

    # Take the ladders in the best path
    for ladder in path:
        steps += count_throws(position, ladder[0], d, snakes)
        print(f"Taking ladder -> {ladder[0]} ---- {ladder[1]}")
        position = ladder[1]

    # Get to 100
    steps += count_throws(position, 100,d,snakes)

    return steps



if __name__ =="__main__":
    print(find_path([(1,38),(4,14),(21,42),(28,84)]))
    snakes = [(31,5),(50,20)]
    print("count:", count_throws(9,41,10,snakes))

    v = part_1(d=6,
               ladders=[(1,38),(4,14),(21,42),(28,84)],
               snakes=[(48,26),(49,11),(62,19),(87,24)])