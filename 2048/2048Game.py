from copy import deepcopy
#from utilities import place_random, print_board
from random import randint
DEV_MODE = False

import random


def print_board(game_board: [[int, ], ]) -> None:
    """
    Print a formatted version of the game board.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    """
    for row in game_board:
        print("+----+" * 4)
        print(''.join(f"|{cell if cell else '':^4}|" for cell in row))
        print("+----+" * 4)


def place_random(game_board: [[int, ], ]) -> {str: int, }:
    """
    Generates a random value and coordinates for the next number to be placed on the board.
    Will raise error if the provided board is full.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: dictionary with the following keys: {'row': int, 'column': int, 'value': int}
    """
    empty_cells = [(y, x) for y, row in enumerate(game_board) for x, cell in enumerate(row) if not cell]
    if not empty_cells:
        raise Exception("Board Full")
    return dict(
        zip(('row', 'column', 'value'), (*random.choice(empty_cells), (2 if random.random() * 100 < 90 else 4))))

############################################### DEFINITIONS ##########################################################################
def new_cell_value(list_numbers, values):
    ''' Makes another random cell in empty space.'''
    random_column = randint(0,3)
    random_row = randint(0,3)
    random_num_list = randint(0,len(list_numbers) - 1)
    random_num = list_numbers[random_num_list]
    if (values[random_row][random_column] == 0):
        values[random_row][random_column] = random_num
    else:
        while (values[random_row][random_column] != 0):
            random_column = randint(0,3)
            random_row = randint(0,3)
        values[random_row][random_column] = random_num


        
def full_board(values):
    ''' Tests if 0 in values.'''
    for list in values:
        if 0 in list:
            return True
    return False
    
def check_row_left(values):
    copy_values = deepcopy(values)
    a_move(copy_values)
    if copy_values == values:
        return True
    return False
    
def check_row_right(values):
    copy_values = deepcopy(values)
    d_move(copy_values)
    if copy_values == values:
        return True
    return False

def check_col(values):
    copy_values = deepcopy(values)
    w_move(copy_values)
    if copy_values == values:
        return True
    return False

def check_col_down(values):
    copy_values = deepcopy(values)
    s_move(copy_values)
    if copy_values == values:
        return True
    return False

            
def change_of_values(values):
    if check_row_left(values) == True:
        return True
    return False
    
def new_list_value(list_numbers, values):
    for list in values:
        for item in list:
            if item not in list_numbers:
                list_numbers.append(item)
    return list_numbers

def game_won(values):
    for list in values:
        if 2048 in list:
            return True
    return False        
    
   
##################### MOVEMENTS##############################################3#

###########################LEFT  MAIN : SHIFT AND COMBINE ######################################3
def shift_items_left(values):
    ''' shifts your items left'''
    stop = 0
    for item in range(4):
        if item != 0:
            if values[0] != 0:
                stop = 0
                if values[1] != 0:
                        stop = 1
                        if values[2] != 0:
                            stop = 2
        while values[item] != 0 and values[item - 1] == 0 and item != stop: ## something went wrong
            values[item - 1] = values[item]
            values[item] = 0
            item -= 1
    return values
    
def combine_left(values):
    ''' Combines all your values left.'''
    number = 0
    for i in range(len(values) - 1):
        if values[i] == values[i + 1]:
            value_values = values[i]
            values[i] = values[i] * 2 #combines alike values
            values[i + 1] = 0
   
    return(values)
    
def a_move(values):
    for list in values:
        shift_items_left(list)
        combine_left(list)
        shift_items_left(list)
    return values


#########################################  USER RIGHT #####################################
def d_move(values):
    ''' values Function for RIGHT.'''
    for list in values:
        list.reverse()
        shift_items_left(list)
        combine_left(list)
        shift_items_left(list)
        list.reverse()
    return values
     
#################################### USER UP & DOWN #####################################################################

def w_move(values):
    ''' Final shift up.'''
    ValuesCopy = []
    for col in range(len(values)):
        list_copy = []
        for row in range(len(values)):
            list_copy.append(values[row][col])
        ValuesCopy.append(list_copy)
    
    a_move(ValuesCopy)
    
    for col in range(4):
        list_back = []
        for row in range(4):
            list_back.append(ValuesCopy[row][col])
        values[col] = list_back
    return values

def s_move(values):
    ''' Final shift down'''
    ValuesCopy = []
    for col in range(len(values)):
        list_copy = []
        for row in range(len(values)):
            list_copy.append(values[row][col])
        ValuesCopy.append(list_copy)
    
    d_move(ValuesCopy)
    
    for col in range(4):
        list_back = []
        for row in range(4):
            list_back.append(ValuesCopy[row][col])
        values[col] = list_back
    return values

#####################################################################################################################################

def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # predefined stuff
    list_numbers = [2]
    
    # Initialize board's first cell
    values = game_board
    #game_over(values) = False
    
    # You are not required to implement develop mode, but it is encouraged to do so.
    # Develop mode allows you to input the location of the next piece that will be
    # placed on the board, rather than attempting to debug your code with random
    # input values.
    if DEV_MODE:
        # This line of code handles the input of the develop mode.
        column, row, value = (int(i) for i in input("column,row,value:").split(','))

        # OPTIONAL: place the piece in the corresponding cell on the game board
    else:
        # TODO: generate a random piece and location using the place_random function
        
        x = place_random(values)
        
        values[x['row']][x['column']] = x['value']
        x = place_random(values)
     
        values[x['row']][x['column']] = x['value']
        
        #game_over(values)
        # TODO: place the piece at the specified location
        pass  
    
           
            

    # Game Loop
    while True: 
        #break
        # TODO: Reset user input variable

        # TODO: Take computer's turn
        # place a random piece on the board
        # check to see if the game is over using the game_over function
        # TODO: Show updated board using the print_board function
        print()
        print_board(values)
        print()
        
        #if game_over(values) == True: 
            #break
        # TODO: Take user's turn
        #else:
        answer = input('input :')
            
            
        
        # Take input until the user's move is a valid keyif
                    
        if  answer == 'w':
            w_move(values)
        
        elif  answer == 'a':
            a_move(values)
            
              
        elif  answer == 's':
            s_move(values)
           
        elif  answer == 'd': 
            d_move(values)
        
        # if the user quits the game, print Goodbye and stop the Game Loop
        elif answer == 'q':
                print("Goodbye")
                break
        
        
        # if user inputs wrong key
        else:
            print(answer,"# note this input is invalid, and therefore the program does not act upon it")
            answer = input()
            while answer != 'w' or answer != 'a' or answer != 's' or answer != 'd' or answer != 'q': 
                print(answer, "# here it rejects the input again, only proceeding when the input is valid")
                answer = input()      
        # Execute the user's move
        game_won(values)
        if game_won(values) == True:
            break  
        
        # Check if the user wins
        #if game_over(values) == False:
        if full_board(values) == True:
            x = place_random(values)
            values[x['row']][x['column']] = x['value']
        
        if game_over(values) == True: 
            
            break
    return values


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    values = game_board
    # TODO: Loop over the board and determine if the game is over
    full_board(values)
    if full_board(values) == False:
        if change_of_values(values) == True:
            print_board(values)
            print('Game Over')
            return True
             #this means game is over
    return False  # TODO: Don't always return false 


if __name__ == "__main__":
    values = ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
    
    main(values)
    
    

    

