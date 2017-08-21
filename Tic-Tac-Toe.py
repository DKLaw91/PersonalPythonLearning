topL=1
topM=2
topR=3
midL=4
midM=5
midR=6
botL=7
botM=8
botR=9

playoptions = [topL, topM, topR, midL, midM, midR, botL, botM, botR]

board = { topL: '1', topM: '2', topR: '3', 
          midL: '4', midM: '5', midR: '6', 
          botL: '7', botM: '8', botR: '9'}
          
def printBoard(board):
  print(board[topL] + '|' + board[topM] + '|' + board[topR])
  print('-+-+-')
  print(board[midL] + '|' + board[midM] + '|' + board[midR])
  print('-+-+-')
  print(board[botL] + '|' + board[botM] + '|' + board[botR])

from random import randint

def playerturn():
  player = playoptions[int(input('where would you like to go?'))]-1
  if player == 1:
    board[topL] = 'x'
  elif player == 2:
    board[topM] = 'x'
  elif player == 3:
    board[topR] = 'x'
  elif player == 4:
    board[midL] = 'x'
  elif player == 5:
    board[midM] = 'x'
  elif player == 6:
    board[midR] = 'x'
  elif player == 7:
    board[botL] = 'x'
  elif player == 8:
    board[botM] = 'x'
  else:
    board[botR] = 'x'
    
    
def cputurn():
  computer = playoptions[randint(0,8)]
  print(computer)
  if computer == 1:
    board[topL] = 'o'
  elif computer == 2:
    board[topM] = 'o'
  elif computer == 3:
    board[topR] = 'o'
  elif computer == 4:
    board[midL] = 'o'
  elif computer == 5:
    board[midM] = 'o'
  elif computer == 6:
    board[midR] = 'o'
  elif computer == 7:
    board[botL] = 'o'
  elif computer == 8:
    board[botM] = 'o'
  else:
    board[botR] = 'o'

cputurn()
playerturn()
printBoard(board)







_________________________________________

topL=1
topM=2
topR=3
midL=4
midM=5
midR=6
botL=7
botM=8
botR=9

player=''
computer=''


playoptions = [topL, topM, topR, midL, midM, midR, botL, botM, botR]

board = { topL: '1', topM: '2', topR: '3', 
          midL: '4', midM: '5', midR: '6', 
          botL: '7', botM: '8', botR: '9'}
          
def printBoard(board):
  print(board[topL] + '|' + board[topM] + '|' + board[topR])
  print('-+-+-')
  print(board[midL] + '|' + board[midM] + '|' + board[midR])
  print('-+-+-')
  print(board[botL] + '|' + board[botM] + '|' + board[botR])

from random import randint

def playerturn():
  player = playoptions[int(input('where would you like to go?'))-1]
  if player == 1:
    board[topL] = 'x'
  elif player == 2:
    board[topM] = 'x'
  elif player == 3:
    board[topR] = 'x'
  elif player == 4:
    board[midL] = 'x'
  elif player == 5:
    board[midM] = 'x'
  elif player == 6:
    board[midR] = 'x'
  elif player == 7:
    board[botL] = 'x'
  elif player == 8:
    board[botM] = 'x'
  else:
    board[botR] = 'x'
    
    
def cputurn():
  cpu = True
  while cpu:
    computer = playoptions[randint(0,8)]
    if computer != player:
      print(computer)
      if computer == 1:
        board[topL] = 'o'
      elif computer == 2:
        board[topM] = 'o'
      elif computer == 3:
        board[topR] = 'o'
      elif computer == 4:
        board[midL] = 'o'
      elif computer == 5:
        board[midM] = 'o'
      elif computer == 6:
        board[midR] = 'o'
      elif computer == 7:
        board[botL] = 'o'
      elif computer == 8:
        board[botM] = 'o'
      else:
        board[botR] = 'o'
      cpu = False
    elif computer == player:
     continue


while True:
  playerturn()
  cputurn()
  printBoard(board)



_________________________________________________________________

topL=1
topM=2
topR=3
midL=4
midM=5
midR=6
botL=7
botM=8
botR=9

player=''
computer=''


board = { topL: '1', topM: '2', topR: '3', 
          midL: '4', midM: '5', midR: '6', 
          botL: '7', botM: '8', botR: '9'}
          
def printBoard(board):
  print(board[topL] + '|' + board[topM] + '|' + board[topR])
  print('-+-+-')
  print(board[midL] + '|' + board[midM] + '|' + board[midR])
  print('-+-+-')
  print(board[botL] + '|' + board[botM] + '|' + board[botR])

from random import randint

def playerturn():
  player = int(input('where would you like to go?'))
  if player == 1:
    board[topL] = 'x'
  elif player == 2:
    board[topM] = 'x'
  elif player == 3:
    board[topR] = 'x'
  elif player == 4:
    board[midL] = 'x'
  elif player == 5:
    board[midM] = 'x'
  elif player == 6:
    board[midR] = 'x'
  elif player == 7:
    board[botL] = 'x'
  elif player == 8:
    board[botM] = 'x'
  else:
    board[botR] = 'x'
    
    
  cpu = True
  while cpu:
    computer = randint(1,9)
    if computer != player:
      print(computer)
      if computer == 1:
        board[topL] = 'o'
      elif computer == 2:
        board[topM] = 'o'
      elif computer == 3:
        board[topR] = 'o'
      elif computer == 4:
        board[midL] = 'o'
      elif computer == 5:
        board[midM] = 'o'
      elif computer == 6:
        board[midR] = 'o'
      elif computer == 7:
        board[botL] = 'o'
      elif computer == 8:
        board[botM] = 'o'
      else:
        board[botR] = 'o'
      cpu = False
    elif computer == player:
     continue

while True:
  playerturn()
  printBoard(board)
