"""
Description: CRC 2026- Prelim 2
Author: Youmna Badawy

What we know:
- For a word to be placed at a given position:
    - One of its letter must be present at that given position
    - The other letters of the word must be placed horizontally or vertically
    in empty spots or spots with the same letter.
    - A placement is favored over another if it's using more letters from the original
    board

Strategy:
Loop over each line in the board
    Loop over each character in the line
        IF the character is found in the letter
            Try to place it top->bottom
            Try to place it bottom -> top
            Try to place it left->right
            Try to place it right -> left
            Count how many other letters of the same word are found for each of the methods above
            Pick the one with the largest score

Details: Trying a given orientation
top-> bottom:
Set the current position in the board -> Position
Find the index of the letter within the word -> index
Find the range of indexes of the word within the board:
    current_y - index : current_y + (len(word) - index + 1)

For e
    If the board at given index is equal to the word[
"""
# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 2.
Ceci est le fichier template pour la partie 2 du Prelim 2.
"""
import copy
Grid = list[list[str]]
Position = tuple[int,int]
def print_grid(grid):
    for line in grid:
        print(" ".join(line))

def search(grid:Grid, word:str)->list[Position]:
    """
    Search for possible positions where the word could be inserted
    """
    possible_positions= [(i,j) for j, line in enumerate(grid) for i,c in enumerate(line) if c in word]

    return possible_positions

DIR_TO_DISP = {
    "top_bottom":(0,1),
    "bottom_top":(0,-1),
    "right_left":(1,0),
    "left_right":(-1,0)
}

def is_within(value, minimum, maximum):
    return minimum <= value <=maximum


def sub_grid_horizontal(grid:Grid, y_pos:int, start:int, stop:int, dir:int)->list[str]:
    """
    Finds a 1D sublist within the grid horizontally (left/right) of any given line.:


    Args:
        grid: NxM list of lists of strings containing the original scrabble board
        y_pos: Index of the line (index of the line in the outer list)
        start: Index of the first character to be included in the list
        stop: Index+1 of last character to be included (stop will NOT be included)
        dir: Direction  1 (left to right) or -1 (right to left)
         * If `dir =1`, the sublist will be formed by reading the characters of the line
         from left to right.
         * If `dir=-1`, the sublist will be formed by reading the characters of the line from
         right to left.
    Returns:
        1D list of strings of the characters
    """

    sub_grid = grid[y_pos][start:stop:dir]
    return sub_grid

def sub_grid_vertical(grid:Grid, x_pos:int,start:int, stop:int, dir:int)->list[str]:
    """
    Finds a 1D sublist within the grid in the vertical direction (top/bottom) of any given column

    Args:
        grid: NxM list of lists of strings containing the original scrabble board
        x_pos: Index of the column (index of the column in the inner lists)
        start: Index of the first character to be included in the list
        stop: Index+1 of the last character to be included in the list
        dir: Direction of the sublist
             * If `dir =1`, the sublist will be formed by reading the characters of the column
         from top to bottom.
            * If `dir=-1`, the sublist will be formed by reading the characters of the column from
         bottom to top.
    Returns:
        1D list of strings of the characters
    """
    sub_grid = []
    for pos in range(start,stop,dir):
        sub_grid.append(grid[pos][x_pos])

    return sub_grid

def explore(grid:Grid, word:str, letter_position:Position) ->list[(int, (Position, Position))]:
    """
    Tests if the word can be placed horizontally or vertically in the board while intersecting the main
    board at a given letter position. For every possible orientation, counts how many letters intersect
    with the main board.

    Args:
        grid: List of lists of strings containing the original scrabble board
        word: The word to be placed in the scrabble board
        letter_position: Position of the letter in the word which could be placed in the scrabble board

    Returns:
        A list of tuples of possible start and end positions with their associated scores (score of how many
        times the word would intersect with the board).
    """

    x, y = letter_position   # in the grid
    letter = grid[y][x]
    grid_height, grid_width = len(grid), len(grid[0])

    letter_pos_in_word = word.index(letter) # in the word

    options = [] #placeholders for all possible orientation that can work for this given letter

    for direction, move in DIR_TO_DISP.items():
        dir_x, dir_y = move



        sub_grid = []       # placeholder of the sub list formed from the grid.
        current_option = () # will be set if an option is possible

        # Vertical
        if dir_y!=0:
            start_y = y - dir_y * letter_pos_in_word
            stop_y = start_y + dir_y * len(word)
            if is_within(start_y, 0, grid_height) and is_within(stop_y, 0, grid_height):
                current_option = ((x,start_y), (x,stop_y))
                sub_grid = sub_grid_vertical(grid,x, start_y, stop_y,dir_y)
            else:
                # not a possible placement
                # restart with the next orientation
                continue

        # Horizontal
        if dir_x!=0:
            start_x = x - dir_x * letter_pos_in_word
            stop_x = start_x + dir_x * len(word)

            if is_within(start_x, 0, grid_width) and is_within(stop_x, 0, grid_width):
                current_option = ((start_x, y), (stop_x, y))
                sub_grid = sub_grid_horizontal(grid,y,start_x, stop_x, dir_x)
            else:
                # not a possible placement
                # restart with the next orientation
                continue

        # counting score for given direction
        # this placement could work
        score = 0

        for char, actual_char in zip(word, sub_grid):
            if char == actual_char:
                # Increment points because letter got intersected
                score+=1
            elif actual_char == " ":
                # Just keep adding letters, but no points scored
                continue
            else:
                # Cannot place the word here
                break
        else:
            # At normal exit of the loop
            # Found an option that works!
            # Let's save it, with the score of words it intersects
            options.append((score, current_option))
    return options

def place(grid:Grid, word:str, start:Position, end:Position):
    x0, y0 = start

    xf, yf = end

    if y0 == yf: # horizontal placement
        dir_x = 1 if x0 <= xf else -1
        grid[y0][x0:xf:dir_x] = word[::dir_x]

    if x0 == xf: # vertical placement

        dir_y = 1 if y0 <= yf else -1

        for y,i in zip(range(y0,yf,dir_y),range(len(word))):
            grid[y][x0] = word[i]

    return grid

def part_2(grid: list[list[str]], word: str):
    """
    Place the world on the Scrabble grid

    Parameters:
        grid [str]: The 10X10 scrabble's grid
        word str: The word to place on the grid

    Returns:
        [str]: The new scrabble's grid with the world place in it
    """
    new_grid = copy.deepcopy(grid)
    ### You code goes here ###
    ### Votre code va ici ###

    potential_positions = search(grid, word)

    possible_placements = []
    for letter_position in potential_positions:
        possible_placements += explore(grid,word,letter_position)

    # because if the word at a given placement intersects the scrabble at
    # multiple locations, these letter will be found multiple times.
    unique_placements = set(possible_placements)

    # Sort in reverse order of the score
    sorted_placements = sorted(unique_placements, key=lambda x: x[0], reverse=True)

    #Find the best placement and place the word
    score, best = sorted_placements[0]

    place(new_grid, word, best[0], best[1])

    return new_grid


if __name__ =="__main__":
    grid = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'U', ' ', 'A', 'W', 'E', 'A', 'R', 'Y', ' '],
        [' ', ' ', 'D', ' ', ' ', ' ', ' ', ' ', 'U', ' ', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' '],
        ['H', 'A', 'R', 'P', 'O', 'O', 'N', ' ', 'T', ' ', ' '],
        [' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' '],
        [' ', 'E', 'L', 'B', 'A', 'R', 'O', 'D', 'A', ' ', ' '],
        [' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', 'R', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ']]

    word = "DOWNPOUR"
    print_grid(grid)
    print(sub_grid_vertical(grid,2,6,2,-1))
    print(sub_grid_horizontal(grid,3,2,9,1))

    solution = part_2(grid,word)
    print_grid(solution)