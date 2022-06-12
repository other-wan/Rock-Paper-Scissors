
import random
from typing import List


def getUserChoice(choices: List[str]) -> str:
    user_input = input("Choose between 'R', 'P' or 'S', \": ").upper()
    while len(user_input) > 1 or user_input not in choices:
        user_input = input(
            "Pls make a valid choice between 'R', 'P' or 'S': ").upper()
    else:
        return user_input


def getComputerChoice(choices: List[str]) -> str:
    return random.choice(choices)


def compareChoice(userChoice: str, compChoice: str) -> bool or None:
    if(userChoice == compChoice):
        return

    if (userChoice == 'R' and compChoice == 'S') or \
        (userChoice == 'P' and compChoice == 'R') or \
            (userChoice == 'S' and compChoice == 'P'):
        return True

    return False


def printResult(userChoice: str, compChoice: str) -> str:
    choice_dict = {'R': "Rock", 'P': "Paper", 'S': "Scissors"}
    print("\n'Player({0}) : CPU({1})'\n".
          format(choice_dict[userChoice], choice_dict[compChoice]))


if __name__ == "__main__":
    print("\n\t *********** Welcome to a game of Rock | Paper | Scissor  ***********")
    print("\t ******** Make a choic of R: Rock, S: Scissors and P: Paper  ********* \n")

    CHOICES = ['R', 'P', 'S']
    while(True):
        compChoice = getComputerChoice(CHOICES)
        userChoice = getUserChoice(CHOICES)
        printResult(userChoice, compChoice)

        res = compareChoice(userChoice, compChoice)
        if res == None:
            print("Game Tied\n")
            continue
        elif res == True:
            print("User wins\n")
            break
        elif res == False:
            print("CPU wins\n")
            break
