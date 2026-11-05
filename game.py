
import random



# COLORS MENU FOR MAKIG IT LOOK GOOD , ILL USE THEM LATER
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"


def number_game():
    secret = random.randint(1 , 100)
    tries = 0

    print()
    print(CYAN + BOLD +  " i picked a number between 1 and 100" + RESET)


    while True:
        guess = input("ur guess>>>")

        try:
            guess = int(guess)
        except ValueError:
            print(RED + BOLD + "please use a number between 1 to 100" + RESET)
            continue

        tries = tries + 1


        if guess < secret:
            print(YELLOW + "too low" + RESET)

        elif guess > secret:
            print(YELLOW + BOLD + "too high")
        else:
            print(GREEN + BOLD + "you got it!!!!!! " + "  " + " it took u " + str(tries) + " tries" + RESET)
            return
def menu():
    while True:
        print()
        print(CYAN + "--------game zone-------" + RESET)
        print( RED + "chose the game and tye the degit")
        print(YELLOW + BOLD + "1" + "  " + RESET + MAGENTA + BOLD + "guess the number" + RESET)


        choice = input(GREEN + BOLD + "chose the desired game>  ")

        if choice == "1":
            number_game()
        else:
            print("chose a appropite option")

menu()