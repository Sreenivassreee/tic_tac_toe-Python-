
"""   Steps
1.printing the Board
2.cheking the player
3.getting input from player
4.validating the input (should be int)
5.checking the empty board or not. 
6.placing the "X" or "O" according to player
7.checking the winning possibilities
        7.1 horizontal
                7.1.1 ( 1 , 2 , 3 ) places
                7.1.2 ( 4 , 5 , 6 ) places
                7.1.3 ( 7 , 8 , 9 ) places
        7.2 Vertical    
                7.2.1 ( 1 , 4 , 7 ) places
                7.2.2 ( 2 , 5 , 8 ) places
                7.2.3 ( 7 , 8 , 9) places
        7.3 Diagonal
                7.3.1 ( 1 , 5 , 9 ) places
                7.3.2 ( 3 , 5 , 7 ) places
8.printing winner
9.printing greeting message

"""

board = []                                                    # Initializing the Board array

for x in range (0, 9) : 
    board.append(str(x + 1))                                  # adding the numbers to array and  incrementing it by '1' as the range is from zero
                                                                        # and the game get's started with 1 and continues till 9.
player_one = True   # used to track the Player turn 
game_over = False   # used to know the status of the game

                        # 1.printing the Board
def print_gameBoard() :
    print("...........")
    print( '|' + board[0] + '|' + board[1] + '|' + board[2] + '|')      # used to print the board on Terminal
    print("...........")
    print( '|' + board[3] + '|' + board[4] + '|' + board[5] + '|')   
    print("...........")
    print( '|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
    print("...........")                                                # used to separate row by row


while not game_over :                                         # Looping throught the conditions to check the game status
    print_gameBoard()                                           # And if the condition is true, it prints the board
    
                        # 2.cheking the player's turn
    if player_one :                                           # used to print the current player
        print( "Player 1:")
    else :
        print( "Player 2:")
                
                        # 3.getting input from the player , 4.validating the input (should be int)
    try:
        user_input = int(input("-------> "))                  # getting the input from the player 
                                                              # input should be of integer type 
    except:
        print("Please enter a valid input")                   # If anything other than integer is entered, 
        continue                                                 # then it throws an error and prints the error message.
    
                        # 5.checking whether the board is empty or not.
                        
    if board[user_input - 1] == 'X' or board [user_input-1] == 'O':    # checking whether the posisiton is empty or not
        print("Wrong move..!!")                                        # its not empty printing the message
        continue
            
                        # 6.placing the X or O according to player
                        
    if player_one :
        board[user_input - 1] = 'X'                           # placing  "X" for the first user 
    else :
        board[user_input - 1] = 'O'                           # placing  "O" for the second user
                                                              # and continues with the same procedure until a person gets the game win

    player_one = not player_one                               # turning the user


                        #7.checking the winning Posibilities
                                
                                                    # 7.1 checking the inputs horizontally

    if (board[0] == board[1] and board[0] == board[2]) :      #  cheking 1,2,3 places and if the three inputs are same, 
        game_over = True                                      #  then the person who entered the last matching position wins the game
                
    if (board[3] == board[4] and board[3] == board[5]) :      # cheking 4,5,6 places 
        game_over = True                                      # making game over
                
    if (board[6] == board[7] and board[6] == board[8]) :      # cheking 7,8,9 places 
        game_over = True                                      # making game over
                        
                        
                        # 7.2 checking the inputs in vertical manner
                        
    if (board[0] == board[3] and board[0] == board[6]) :      # cheking 1,4,7 places
        game_over = True                                      # making game over
                
    if (board[1] == board[4] and board[1] == board[7]) :      # cheking 2,5,8 places
        game_over = True                                      # making game over
                
    if (board[2] == board[5] and board[2] == board[8]) :      # cheking 3,6,9 places
        game_over = True                                      # making game over
                        
                        
                        # 7.3 validating the inputs diagonally
                                             
    if((board[0] == board[4] and board[0] == board[8]) or (board[2] == board[4] and board[4] == board[6])) :
                                                              # cheking 1,5,9 and 3,5,7 places
        game_over = True                                      # making game over
                        # 8.printing winner 
                        
print ("Player " + str(int(player_one + 1)) + " wins")        # Announcing  the winner

                        # 9.printing greeting message
                        
print ("Thanks for playing")                                  # printing greeting message
                
