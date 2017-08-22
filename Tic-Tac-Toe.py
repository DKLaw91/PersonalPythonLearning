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
          
def cpuwin(board):
  if board[topL] and board[topM] and board[topR] == 'o':
    print('You lose. Better luck next time.')
  elif board[topL] and board[midM] and board[botR] == 'o':
    print('You lose. Better luck next time.')
  elif board[topL] and board[midL] and board[botL] =='o':
    print('You lose. Better luck next time.')
  elif board[midL] and board[midM] and board[midR] == 'o':
    print('You lose. Better luck next time.')
  elif board[botL] and board[botM] and board[botR] == 'o':
    print('You lose. Better luck next time.')
  elif board[topR] and board[midM] and board[botL] == 'o':
    print('You lose. Better luck next time.')
  elif board[topM] and board[midM] and board[botM] == 'o':
    print('You lose. Better luck next time.')
  elif board[topR] and board[midR] and board[botR] == 'o':
    print('You lose. Better luck next time.')
  else:
    print('')
    
   
def playerwin(board):    
  if board[topL] and board[topM] and board[topR] == 'x':
    print('You win! Well played.')
  elif board[topL] and board[midM] and board[botR] == 'x':
    print('You win! Well played.')
  elif board[topL] and board[midL] and board[botL] == 'x':
    print('You win! Well played.') 
  elif board[midL] and board[midM] and board[midR] == 'x':
    print('You win! Well played.')
  elif board[botL] and board[botM] and board[botR] == 'x':
    print('You win! Well played.')
  elif board[topR] and board[midM] and board[botL] == 'x':
    print('You win! Well played.')
  elif board[topM] and board[midM] and board[botM] == 'x':
    print('You win! Well played.')
  elif board[topR] and board[midR] and board[botR] == 'x':
    print('You win! Well played.')    
  else:
    print('')


def printBoard(board):
  print(board[topL] + '|' + board[topM] + '|' + board[topR])
  print('-+-+-')
  print(board[midL] + '|' + board[midM] + '|' + board[midR])
  print('-+-+-')
  print(board[botL] + '|' + board[botM] + '|' + board[botR])

from random import randint

def playerturn(player):
  correctValue = True
  while correctValue:
    player = int(input('where would you like to go?'))
    if str(player) in board.values():
      board[player] = 'x'
      correctValue=False
    else:
      input('Place on board already taken, please choose again.')
      continue
  playerwin(board)
      
def cputurn(computer):    
  cpu = True
  while cpu:
    computer = randint(1,9)
    if str(computer) in board.values():
      if computer != player:
        input('CPU: ' + str(computer))
        board[computer] = 'o'
      cpu = False
    else:
      continue
  cpuwin(board)
  

while True:
  playerturn(player)
  printBoard(board)
  cputurn(computer)
  printBoard(board)
          
          
  _____________________________________________

from random import randint

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
 
def winner():
  if board[topL]== 'x':
    if board[topM]=='x':
      if board[topR]=='x':
        print('you win.')
    if board[midM]=='x':
      if board[botR]=='x':
        print('you win.')
    if board[midL]=='x':
      if board[botL]=='x':
        print('you win.')          
          
def printBoard():
  print(board[topL] + '|' + board[topM] + '|' + board[topR])
  print('-+-+-')
  print(board[midL] + '|' + board[midM] + '|' + board[midR])
  print('-+-+-')
  print(board[botL] + '|' + board[botM] + '|' + board[botR])


def playerturn():
  correctValue = True
  while correctValue:
    player = int(input('where would you like to go?'))
    if str(player) in board.values():
      board[player] = 'x'
      correctValue=False
    else:
      input('Place on board already taken, please choose again.')
      continue
      
      
def cputurn():    
  cpu = True
  while cpu:
    computer = randint(1,9)
    if str(computer) in board.values():
      if computer != player:
        input('CPU: ' + str(computer))
        board[computer] = 'o'
      cpu = False
    else:
      continue


while True:
  playerturn()
  printBoard()
  cputurn()
  printBoard()

