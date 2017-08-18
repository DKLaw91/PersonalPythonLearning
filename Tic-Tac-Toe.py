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

board = { topL: ' ', topM: ' ', topR: ' ', 
          midL: ' ', midM: ' ', midR: ' ', 
          botL: ' ', botM: ' ', botR: ' '}
          
def printBoard(board):
  print(board[topL] + '|' + board[topM] + '|' + board[topR])
  print('-+-+-')
  print(board[midL] + '|' + board[midM] + '|' + board[midR])
  print('-+-+-')
  print(board[botL] + '|' + board[botM] + '|' + board[botR])

from random import randint


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


printBoard(board)
