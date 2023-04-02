import random, os

list_of_options = ["rock", "scissors", "paper"]


#This function is the function that determines how many rounds the user wants to play. I did it this way because I wanted to ID10T proof it. I did this using try and except which tried to take the integer of the input. If it wasn't possible, the program would display an error message and try again.
def rounds():
  while True:
    try:
      inp = int(input("How many rounds do you want to play? "))
      break
    except:
      print("Invalid Entry. Try again")

  if inp < 0:  #In this algorithm I tested if the input was less than 0. If it was, I displayed an error message and looped the program. If it  wasn't, the main program was run. I did this in order to ID10T proof the program so that there couldn't be negative rounds.
    print("You cannot have negative rounds!")
    rounds()
  else:
    game(inp)


def game(
  numrounds
):  #In this function, I tested the value of the numrounds parameter as wether or not it was 0. If it was, it ended the program and displayed a "Goodbye" message. If it wasn't, it continued on. I did it this way, so that the entire game would end if the user chose not to play. This is because the function returns a value which stops the program from continuing the function.
  if numrounds == 0:
    print("You have chosen not to play.")
    return ("no")
  compscore = 0
  playscore = 0
  for i in range(numrounds):
    while True:
      opt = input("Pick one: Rock, Paper or Scissors: ")
      opt = opt.lower()
      print("")
      if opt == "rock" or opt == "paper" or opt == "scissors":
        cc = random.choice(
          list_of_options
        )  #Here I used the imported random module for the computer's choice to be random from the options in list_of_options. I did this because it manages complexity of the program so that it takes less code to determine the computer's option.
        print(f"The computer chose: {cc}")
        winner = result(opt, cc)

        if winner == "compscore":
          compscore += 1

        elif winner == "playscore":
          playscore += 1

        print(f"Current score\n Player: {playscore}  Computer: {compscore} \n")
        break
      else:
        print("Invalid entry. Try again!")

  print(f"Final Score: \n Player: {playscore}  Computer: {compscore}")
  again()


def result(
  opt, cc
):  #In this function, I used math to determine the winner of the rock paper scissors. Based on the list "list_of_options", if the computer's choice was 1 index more or 2 index less than the user's choice, the user would win. However, if both indexes are the same, it results in a draw. Lastly, if none of the previous conditions are true the user would lose. I did it this way because it managed complexity of the program by using less code to determine the winner.
  if list_of_options.index(opt) == list_of_options.index(
      cc) - 1 or list_of_options.index(opt) == list_of_options.index(cc) + 2:
    print("You Won!")
    return "playscore"
  elif list_of_options.index(opt) == list_of_options.index(cc):
    print("It's a draw")
  else:
    print("You Lost!")
    return "compscore"


def again():
  inp = input("Do you want to play again? y or n: ")
  if inp.lower() == 'yes' or inp.lower() == 'y':
    os.system('clear')
    rounds()
  elif inp.lower() == 'no' or inp.lower() == 'n':
    return "no"
  else:
    print("Invalid Entry. Try again!")
    again()


print("Welcome to this Rock Paper Scissors game!\n")
rounds()
print("Goodbye!")
