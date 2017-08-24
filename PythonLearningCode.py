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
game=True


board = { topL: '1', topM: '2', topR: '3', 
          midL: '4', midM: '5', midR: '6', 
          botL: '7', botM: '8', botR: '9'}

          
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


while game:
  playerturn()
  printBoard()
  
  
  if board[topL]== 'x':
    if board[topM]=='x':
      if board[topR]=='x':
        print('you win.')
        game=False
        break
    if board[midM]=='x':
      if board[botR]=='x':
        print('you win.')
        game=False
        break
    if board[midL]=='x':
      if board[botL]=='x':
        print('you win.')
        game=False
        break
  elif board[midL]=='x':
    if board[midM]=='x':
      if board[midR]=='x':
        print('you win.')
        game=False
        break
  elif board[botL]=='x':
    if board[botM]=='x':
      if board[botR]=='x':
        print('you win.')
        game=False
        break
    if board[midM]=='x':
      if board[topR]=='x':
        print('you win.')
        game=False
        break
  elif board[botM]=='x':
    if board[botL]=='x':
      if board[botR]=='x':
        print('you win.')
        game=False
        break
    elif board[topM]=='x':
      if board[midM]=='x':
        print('you win.')
        game=False
        break
  elif board[botR]=='x':
    if board[midR]=='x':
      if board[topR]=='x':
        print('you win.')
        game=False
        break
  
  
  cputurn()
  printBoard()
  
  
  if board[topL]== 'o':
    if board[topM]=='o':
      if board[topR]=='o':
        print('you lose.')
        game=False
    if board[midM]=='o':
      if board[botR]=='o':
        print('you lose.')
        game=False
    if board[midL]=='o':
      if board[botL]=='o':
        print('you lose.')
        game=False
  elif board[midL]=='o':
    if board[midM]=='o':
      if board[midR]=='o':
        print('you lose.')
        game=False
  elif board[botL]=='o':
    if board[botM]=='o':
      if board[botR]=='o':
        print('you lose.')
        game=False
    if board[midM]=='o':
      if board[topR]=='o':
        print('you lose.')
        game=False
  elif board[botM]=='o':
    if board[botL]=='o':
      if board[botR]=='o':
        print('you lose.')
        game=False
    elif board[topM]=='o':
      if board[midM]=='o':
        print('you lose.')
        game=False
  elif board[botR]=='o':
    if board[midR]=='o':
      if board[topR]=='o':
        print('you lose.')
        game=False
