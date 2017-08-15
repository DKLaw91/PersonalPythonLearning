# PersonalPythonLearning
Storage for code used whilst learning Python


def RockPaperScissors():

  from random import randint
 
  t = ['Rock', 'Paper', 'Scissors']
 
  computer = t[randint(0,2)]
 
  player = False
 
  playcount = 0
 
  while player == False:
    for i in range (3):
      player = input ('Rock, Paper, Scissors?')
      player = player.strip()
      print(computer + '!')
      if player.lower() == computer.lower():
        print('Tie!')
      elif player.lower() == 'rock':
        if computer == 'Paper':
          print('You lose! ', computer, ' covers ', player)
        else: print('You win!', player, 'smashes ', computer)
      elif player.lower() == 'paper':
        if computer == 'Scissors':
          print('You lose! ', computer, ' cut ', player)
        else: print('You Win! ', player, ' covers ', computer)
      elif player.lower() == 'scissors':
        if computer == 'Rock':
          print('You lose! ', computer, ' smashes ', player)
        else:
          print('You win! ', player, ' cut ', computer)
      else:
        print('Try again!')
      playcount = playcount + 1
      player = False
      computer = t[randint(0,2)]
    
    playagain = input('Shall we play again?')
    if playagain == 'no':
      print('Okay :( Goodbye!')
      print('Returning to welcome screen...')
      print('...')
      break
    else:
      player = False
      computer = t[randint(0,2)]
      playcount = 0

def intro():
 
  import sys
 
 
  while True:
    try:
      print('Welcome. Which option would you like to use? 1. Rock, Paper, Scissors 2. Exit')
      option = int(input())
    except:
      print('Please use numeric value (1, 2, 3, etc.)')
      continue
    if option == 1:
      print('Starting Rock, Paper, Scissors...')
      print('...')
      RockPaperScissors()
    elif option == 2:
      userexit = ()
      while userexit != 'y' or 'n':
        userexit = input('Are you sure you want to exit? Y/N')
        if userexit.lower() == 'y':
           sys.exit()
        elif userexit.lower() == 'n':
           print('Returning to welcome screen...')
           print('...')
           break
        else:
         print('Invalid input. Please use Y for Yes or N for No.')
    
intro()
      
