"""
Author: Youmna Badawy
Description: Solving a 2D problem where a platypus marked as "X" looks
for food marked as "." in a list of N strings of width M with empty spaces "_", "x" and "."
characters.
The solution proposed here, uses a sorted list of tuples containing the manhattan distance
between the "x" and all the foods ("." characters on the board) as well as the coordinates
of each food ".".
It then moves the platypus "x" according to rules of priority described in the Prelims part 5.

If distance is 1 and there's multiple foods around:
    - Move right has higher priority
    - Move down has second highest priority
    - Move left has third priority
    - Move up has least priority

If foods are too far,
   - Sort by distance
   - Prioritize horizontal movements (along x), so we sort by x next
   - Then vertical movements (along y)

Why tuples are ideal structure for this problem:
Because we can sort a list of tuples and it will also prioritize the first item x:
(x,y) in ascending order, then y.

Why list comprehensions are good for 2D problems. These style problems often require
nested for loops which isn't computationally efficient in general. Using list comprehension
uses a c-level for loop which runs much fast for these styles of questions.
"""
Position = (int,int)
Board = [[list]]
def find_char(board:Board, char:str)->list[Position]:
    """Scans the board to find all the position where a given character is found"""
    coords = [(x,y) for y,line in enumerate(board) for x,c in enumerate(line) if c == char]
    return coords

def manhattan(coord1:Position, coord2:Position)->int:
    """Calculates the manhattan distance between two positions
    d = |x1 - x2| + |y1 - y2|
    """
    x1,y1 = coord1
    x2,y2 = coord2

    return abs(x1-x2) + abs(y1-y2)

def displacement(start:Position, end:Position)->Position:
    """
    Calculates the delta_x and delta_y to go from a start to an end position

    Returns: A displacement vector (delta_x, delta_y)
    """

    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]

    return (delta_x, delta_y)

def sort_foods(foods:list[Position], platypus:Position)->list[(int,Position)]:
    distances = [manhattan(platypus, food) for food in foods]
    dist2food = [(d,f) for d,f in zip(distances, foods)]
    dist2food.sort()
    return dist2food

def right(platypus:Position)->Position:
    return (platypus[0]+1, platypus[1])

def down(platypus:Position)->Position:
    return (platypus[0], platypus[1]+1)

def left(platypus:Position)->Position:
    return (platypus[0]-1, platypus[1])

def up(platypus:Position)->Position:
    return (platypus[0], platypus[1]-1)

def nearest(sorted_foods:list[(int,Position)], platypus:Position):
    """
    Based on the sorted_foods list sorted by manhattan distance, this extracts
    all the foods at the same distance from the platypus and returns the one
    to prioritize based on the priority of movements of the platypus (left/right), then
    (up/ down)
    """
    smallest_d = sorted_foods[0][0]

    # Extract all the foods at the same smallest distance
    nearest_foods = [food[1] for food in sorted_foods if food[0] == smallest_d]

    # Gets the displacement vector

    # Sorting based on the displacement tuple delta_x, delta_y
    # This will prioritize smaller delta_x (left/right movements)
    # then, smaller delta_y (top/bottom movements)

    sorted_nearest = sorted(nearest_foods, key=lambda f: displacement(platypus,f))

    # Note: This can be further simplified by calculating the

    # Get the best next option
    best_option = sorted_nearest[0]


    return best_option

def print_board(board:Board):
    """Used for debugging purposes"""
    print("BOARD:")
    print("\n".join(("".join(line) for line in board)))
    print("---------------------------------")


def part_5(turns: int, board: [str]):
    """
    Simulate the Game of platypus

    Parameters:
        turns str: The number of turns in the game
        board [str]: The 16x16 grid representing the board of the Game of platypus with x as the platypus and . the food

    Returns:
        str: Is the platypus surviving ("Yes" or "No")
    """
    final_answer = "No"
    ### You code goes here ###
    ### Votre code va ici ###
    test_board = [list(line) for line in board]
    platypus_position = find_char(test_board,"x")
    if not platypus_position:
        print("Error! There is no 'x' on the board")
    if len(platypus_position) >1:
        print("Error! There can't be more than one 'x' on the board")
        return
    platypus = platypus_position[0]

    attempts = 3
    for _ in range(turns):
        print_board(test_board)
        foods = find_char(test_board, '.')
        dist2foods = sort_foods(foods,platypus)
        xp, yp = platypus
        if (1, right(platypus)) in dist2foods:
            "First priority moving up"
            attempts = 3
            new_x, new_y = right(platypus)

        elif (1,down(platypus)) in dist2foods:
            "Second priority moving down"
            attempts = 3
            new_x, new_y = down(platypus)
        elif (1, left(platypus)) in dist2foods:
            "Third priority moving left"
            attempts = 3
            new_x, new_y = left(platypus)
        elif (1, up(platypus)) in dist2foods:
            "Fourth priority moving down"
            attempts = 3
            new_x, new_y = up(platypus)
        else:
            "No food in immediate surroundings"
            attempts -= 1
            best = nearest(dist2foods, platypus)
            delta_x, delta_y = displacement(platypus, best)
            if delta_x != 0: # moving only horizontally by 1
                delta_x, delta_y = delta_x//abs(delta_x), 0

            else: # moving only vertically  by 1
                delta_x, delta_y = 0, delta_y//abs(delta_y)

            new_x, new_y = xp + delta_x, yp+delta_y

        # Moving the platypus
        print("Platypus moved")
        test_board[yp][xp] = "_"
        test_board[new_y][new_x]= "x"
        platypus = (new_x, new_y)

        if attempts ==0:
            break

    if attempts >0 :
        final_answer= "Yes"

    return final_answer


if __name__ == "__main__":
    test_board = [
        "__________",
        "__________",
        "____._____",
        "__________",
        "____x____",
        "__________",
        "__________",
        "__________",
        "____._____"
    ]



    print(part_5(4, test_board))