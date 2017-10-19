def guessgame():
  from random import randint
  secretNumber = randint(1, 20)
  print('I am thinking of a number between 1 and 20. You have 6 guesses.')

  for guessesTaken in range(1, 7):
      guess = int(input('Take a guess.'))

      if guess < secretNumber:
          print('Your guess is too low.')
      elif guess > secretNumber:
          print('Your guess is too high.')
      else:
          break

  if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
  else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


def jokes():
    from random import randint

    def jk1():
        joke = input('What is brown and sounds like a bell?')
        joke = joke.lower()
        if joke.strip() == 'dung':
            print('Ba dum tsh! Beaten to the punch line.')
        else:
            print('Dung!')

    def jk2():
        joke = input('Where did Sally go after the explosion?')
        joke = joke.lower()
        if joke.strip() == 'everywhere':
            print('Ba dum tsh! Beaten to the punch line.')
        else:
            print('Everywhere!')
        answer = True
        while answer == True:
            joke2 = input('Knock, Knock.')
            joke2 = joke2.lower()
            if joke2.strip() == "whos there?" or "who's there?" or 'whos there':
                print('Not Sally!')
                answer = False
            else:
                print('Come on. You know the drill.')

    t = [jk1, jk2]
    computer = t[randint(0, 1)]


    computer()


def mathtrick():
    Numb = int(input('Pick a number, any number:'))
    print('Good choice. Now I can turn your number into the number 3, just watch.')
    input('Take your number & add 5. That gives us:')
    Numb1 = Numb + 5
    print(Numb1)
    input('Multiply that by 2:')
    Numb2 = Numb1 * 2
    print(Numb2)
    input('Now subtract 4:')
    Numb3 = Numb2 - 4
    print(Numb3)
    input('Divide by 2:')
    Numb4 = Numb3 // 2
    print(Numb4)
    input('And lastly, subtract the original number:')
    Numb5 = Numb4 - Numb
    print(Numb5)
    print('Voila!')


def wordplay():
    print('Enter ANYTHING you want!')
    inp1 = input('What is a funny name:')
    inp2 = input('Where is a funny place:')
    inp3 = input('What is a funny activity:')
    inp4 = input('Another funny name:')
    print('There once was a ' + inp1)
    print('From ' + inp2)
    print('Who liked to ' + inp3)
    print('Never have you seen such a ' + inp4)


def RockPaperScissors():
    from random import randint

    t = ['Rock', 'Paper', 'Scissors']

    computer = t[randint(0, 2)]

    player = False

    while player == False:
        for i in range(3):
            player = input('Rock, Paper, Scissors?')
            player = player.strip()
            print(computer + '!')
            if player.lower() == computer.lower():
                print('Tie!')
            elif player.lower() == 'rock':
                if computer == 'Paper':
                    print('You lose! ', computer, ' covers ', player)
                else:
                    print('You win!', player, 'smashes ', computer)
            elif player.lower() == 'paper':
                if computer == 'Scissors':
                    print('You lose! ', computer, ' cut ', player)
                else:
                    print('You Win! ', player, ' covers ', computer)
            elif player.lower() == 'scissors':
                if computer == 'Rock':
                    print('You lose! ', computer, ' smashes ', player)
                else:
                    print('You win! ', player, ' cut ', computer)
            else:
                print('Try again!')
            player = False
            computer = t[randint(0, 2)]
        playagain = input('Shall we play again?')
        if playagain == 'no':
            print('Okay :( Goodbye!')
            print('Returning to welcome screen...')
            print('...')
            break
        else:
            player = False
            computer = t[randint(0, 2)]
            playcount = 0


def calculator():
    def add(num1, num2):
        return num1 + num2
    def subtract(num1, num2):
        return num1 - num2
    def multiply(num1, num2):
        return num1 * num2
    def divide(num1, num2):
        return num1 // num2

    def main():
        validinput = False
        while validinput == False:
            try:
                num1 = int(input('Pick 1st number:'))
                num2 = int(input('Pick 2nd number:'))
                operation = int(input('What would you like to do? 1. Add 2. Subtract 3. Multiply 4. Divide'))
                validinput = True
            except:
                print('Invalid input. Try again.')
                return
            if operation == 1:
                print(add(num1, num2))
            elif operation == 2:
                print(subtract(num1, num2))
            elif operation == 3:
                print(multiply(num1, num2))
            else:
                print(divide(num1, num2))
            playagain = int(input('Do you want to calculate more numbers? 1. Yes 2. No'))
            if playagain == 2:
                print('Okay :( Goodbye!')
            else:
                validinput = False


    main()


def intro():
    import sys

    while True:
        try:
            print('Welcome. Which option would you like to use? 1. Rock, Paper, Scissors 2. Word Game 3. Basic '
                  'Calculator 4. Math Trick 5. Guess The Number Game 6. Tell me a Joke 7. Exit')
            option = int(input())
        except:
            print('Please use numeric value (1, 2, 3, etc.)')
            continue
        if option == 1:
            print('Starting Rock, Paper, Scissors...')
            print('...')
            RockPaperScissors()
        elif option == 2:
            print('Starting Word Game...')
            print('...')
            wordplay()
        elif option ==3:
            print('Starting Basic Calculator...')
            print('...')
            calculator()
        elif option == 4:
            print('Starting Math Trick...')
            print('...')
            mathtrick()
        elif option == 5:
            print('Starting Guess The Number Game...')
            print('...')
            guessgame()
        elif option ==6:
            print('Get ready for a joke!...')
            print('...')
            jokes()
        elif option == 7:
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


topL = 1
topM = 2
topR = 3
midL = 4
midM = 5
midR = 6
botL = 7
botM = 8
botR = 9

player = ''
computer = ''

board = {topL: '1', topM: '2', topR: '3',
         midL: '4', midM: '5', midR: '6',
         botL: '7', botM: '8', botR: '9'}


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
            correctValue = False
        else:
            input('Place on board already taken, please choose again.')
            continue


def cputurn(computer):
    cpu = True
    while cpu:
        computer = randint(1, 9)
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


def checkBoard(board):
    if board[topL] and board[topM] and board[topR] == 'o':
        print('You lose. Better luck next time.')
    elif board[topL] and board[midM] and board[botR] == 'o':
        print('You lose. Better luck next time.')
    elif board[topL] and board[midL] and board[botL] == 'o':
        print('You lose. Better luck next time.')

    elif board[topL] and board[topM] and board[topR] == 'x':
        print('You win! Well played.')
    elif board[topL] and board[midM] and board[botR] == 'x':
        print('You win! Well played.')
    elif board[topL] and board[midL] and board[botL] == 'x':
        print('You win! Well played.')


while True:
    playerturn(player)
    cputurn(computer)
    printBoard(board)



