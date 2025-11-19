""" one-player version of classic board game Battleship.
A single ship will be hidden in a random location in the 5x5 board and the player has to guess the location of the ship."""


from random import randint 

# Create an empty list board

board = []


# Create a 5x5 grid initialized to all O's and store it in board

for i in range(5):
  board.append(['O'] * 5)

def print_board(board_in):
  for row in board:
    print row

print(print_board(board))



# Define two new functions: random_row and random_col, that each take board_in as input.
# These functions should return a random row index and a random column index from your board, respectively.


def random_row(board_in):
  return randint(0, len(board_in)-1)

def random_col(board_in):
  return randint(0, len(board_in)-1)

#print(random_row(board))
#print(random_col(board))


ship_row = random_row(board)
ship_col = random_col(board)


# Print the value of ship_row. Print the value of ship_col.

print(ship_row)
print(ship_col)


# Make sure the player gets only 5 guesses. So, everything from here needs to go in a loop.

for Turn in range(4):
  

# Create a new variable called guess_row and set it to int(raw_input("Guess Row: ")). 
# Create a new variable called guess_col and set it to int(raw_input("Guess Col: ")).

  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  

# add an if to check if guess_row equals ship_row and guess_col equals ship_col. 
# If that is the case, please print out "Congratulations! You sank my battleship!"
# If not prompt the user for another guess.

  
  if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! You sunk my battleship!"
      break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    print "Turn: ", Turn+1
    print_board(board)
    if Turn == 3:
      print("Game Over")
