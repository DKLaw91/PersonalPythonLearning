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
  correctValue = True
  while correctValue:
    player = int(input('where would you like to go?'))
    if str(player) in board.values():
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
      correctValue=False
    else:
      input('Place on board already taken, please choose again.')
      continue
      
    
  cpu = True
  while cpu:
    computer = randint(1,9)
    if str(computer) in board.values():
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
    else:
      continue
  


while True:
  playerturn()
  printBoard(board)
