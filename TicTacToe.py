# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:12:15 2020

@author: James.Thomas
Tic Tac Toe Game
"""
# Tic-Tac-Toe
# Hans Fangohr, University of Southampton, UK
import random
game_on = True
marker = ' '
position = ' '
player1_turn = True




def display_board(board):
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+--')
    print(board[4]+'|'+board[5]+'|'+board[6])  
    print('-+-+--')
    print(board[1]+'|'+board[2]+'|'+board[3])  
    P
def player_input(marker):
    marker = ' '
    while marker not in ('X','O'):
        marker = input('Player 1.  Please choose "X" or "O": ')
        marker = marker.upper()
    return marker   
    
def place_marker(board, marker, position):
    board[position] = marker

#Check if anyone won the game
def win_check(board, mark):
    
    if (board[1] == mark and board[2]== mark and board[3]==mark): 
        return True
    elif (board[4] == mark and board[5]== mark and board[6]==mark): 
        return True
    elif (board[7] == mark and board[8]== mark and board[9]==mark): 
        return True
    elif (board[1] == mark and board[4]== mark and board[7]==mark): 
        return True
    elif (board[2] == mark and board[5]== mark and board[8]==mark):
        return True
    elif (board[3] == mark and board[6]== mark and board[9]==mark):
        return True
    elif (board[1] == mark and board[5]== mark and board[9]==mark):
        return True
    elif (board[3] == mark and board[5]== mark and board[7]==mark):
        return True
    else:
        return False

# Which player goes first 1 or 2 ?
def choose_first():
    return random.randint(1,2)

# Return True if a space on the board is freely available.
def space_check(board, position):
    return board[position] == ' '


# function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    
    return board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '
 



# function that asks for a player's next position (as a number 1-9) 
# and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
         #Initial
    space_ok = False    
    choice = 'WRONG'
    acceptable_range = range(1,9+1)
    within_range = False   

        
    while choice.isdigit() == False or within_range == False or space_ok == False:
        choice = input('What position do you want? (1 - 9): ')
        
        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit")
        
        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False 
                print("Please enter 1 to 9")


        # SPACE AVAILABLE CHECK
        if choice.isdigit() == True:            
            if within_range == True:
                space_ok = space_check(board,int(choice))
                #print(f'space_ok: {space_ok}')
          
                    
    return int(choice)  

# Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    play_again = input('Would you like to play again? (Y/N): ')
    play_again = play_again.upper()
    if play_again == 'Y':
        return True
    else:
        return False



#--------------------------------------------------------------------
#--------------------------------------------------------------------



print('Welcome to Tic Tac Toe!')

while True:
    
    p1_marker = player_input(marker.upper())
        
    if p1_marker == 'X':
        p2_marker = 'O'
    else: 
        p1_marker = 'O'
        p2_marker = 'X'
    
    # Set the game up here
    print('\n'*100) 
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)

     
  


    while game_on:
        if player1_turn:
            marker = p1_marker
            position = player_choice(board)
            place_marker(board, marker, position)
            player1_turn = False
            print('\n'*100) 
            display_board(board)
        else:
            marker = p2_marker
            position = player_choice(board)
            place_marker(board, marker, position)
            player1_turn = True
            print('\n'*100) 
            display_board(board)
 
        if win_check(board, marker):
            print(f'{marker} You win!!')
            break 
                  
            
        if full_board_check(board):
            print("Cat's Game!")
            break
          
            
            
        
        
    if not replay():
        break
    else:
        print(f'Player{choose_first()} goes first')



































