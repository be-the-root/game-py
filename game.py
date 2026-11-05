
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



def rock_game():
    print()
    print(CYAN + BOLD + "rock paper scissors - first to 3 wins" + RESET)


    wins = 0
    losses = 0

    while wins < 3 and losses < 3:
        player = input("rock, paper or scissors>>> ").lower()

        if player != "rock" and player != "paper" and player != "scissors":
            print(RED + BOLD + "thats not a move" + RESET)


        computer = random.choice(["rock" , "paper" , "scissors"])
        print(MAGENTA + BOLD + "computer picked " + RESET)
        
        if player == computer:
            print(YELLOW + BOLD + "tiee" + RESET)
        elif player == "rock" and computer == "scissors":
            wins = wins + 1
        elif player == "paper" and computer == "rock":
            wins =wins + 1
            print(GREEN + "u win that round" + RESET)
        elif player == "scissors" and computer == "paper":
            wins = wins + 1
            print(GREEN + BOLD + "u won tlhis round" + RESET)
        else:
            losses = losses +1
            print(RED + BOLD + "you lost this round" + RESET)

        print("score : u" + str(wins)  + "  -  " + str(losses) + "computer")

    if wins == 3:
        print(GREEN + BOLD + " u won the match!!!!11" + RESET)
    else:
        print(RED + BOLD + "computer won , rematch????" + RESET)            
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
        print(YELLOW + BOLD + "2" + "  " + RESET + MAGENTA + BOLD + "quit"+ RESET)


        choice = input(GREEN + BOLD + "chose the desired game>  ")

        if choice == "1":
            number_game()
        elif choice == "2":
            print("bye!!!")
            break
        elif  choice == "3":
            rock_game()
        else:
            print("chose a appropite option")

menu()