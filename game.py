
# COLORS MENU FOR MAKIG IT LOOK GOOD , ILL USE THEM LATER
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

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