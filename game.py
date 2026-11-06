
import random

RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"


def scramble_game():
    words = ["python", "antique", "guitar", "planet", "castle", "dragon", "silver", "garden"]


    print()
    print(CYAN + BOLD + "word scramble - unscramble 3 words" + RESET)
    print()

    score = 0
    rounds = 3
    for i in range(rounds):
        word = random.choice(words)

        letters = list(word)
        random.shuffle(letters)

        scrambled = ""
        for ch in letters:
            scrambled = scrambled + ch

        tries = 0
        while scrambled == word and tries < 20:
            random.shuffle(letters)
            scrambled = ""
            for ch in letters:
                scrambled = scrambled + ch
            tries = tries + 1
        print(MAGENTA + BOLD + "round " + str(i + 1) + " of " + str(rounds) + RESET)
        print(YELLOW + BOLD + "  scrambled word: " + scrambled + RESET)

        guess = input(GREEN + BOLD + "  ur guess>>> " + RESET ).strip().lower()

        if guess == word:
            score = score + 1
            print(GREEN + BOLD + "   correct" + RESET)
        else:
            print(RED + BOLD + "  nope, it was:  " + word + RESET)


    print(CYAN + BOLD + " you got " + str(score) + " out of " + str(rounds) + RESET)

    if score == rounds:
        print(GREEN + BOLD + " perfect score!!!" + RESET)
    elif score >= 2:
        print(YELLOW + BOLD + " not badd" + RESET )
    else:
        print(RED + BOLD + "study ur words lol" + RESET)

    
def rock_game():
    print()
    print(CYAN + BOLD + "rock paper scissors - first to 3 wins" + RESET)


    wins = 0
    losses = 0

    while wins < 3 and losses < 3:
        player = input(CYAN + BOLD + "rock (r), paper (p) or scissors (s)>> " + RESET).lower()

        if player != "r" and player != "p" and player != "s":
            print(RED + BOLD + "thats not a move" + RESET)


        computer = random.choice(["rock" , "paper" , "scissors"])
        print(MAGENTA + BOLD + "computer picked " + RESET)
        
        if player == computer:
            print(YELLOW + BOLD + "tiee" + RESET)
        elif player == "r" and computer == "scissors":
            wins = wins + 1
            print(GREEN + BOLD + "u won!!!!" + RESET)
        elif player == "p" and computer == "rock":
            wins =wins + 1
            print(GREEN + "u win that round" + RESET)
        elif player == "s" and computer == "paper":
            wins = wins + 1
            print(GREEN + BOLD + "u won tlhis round" + RESET)
        else:
            losses = losses +1
            print(RED + BOLD + "you lost this round" + RESET)

        print(GREEN + BOLD + "score : u" + str(wins)  + "  -  " + str(losses) + "computer" + RESET)

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
        guess = input(GREEN + BOLD + "ur guess>>>" + RESET)

        try:
            guess = int(guess)
        except ValueError:
            print(RED + BOLD + "please use a number between 1 to 100" + RESET)
            continue

        tries = tries + 1


        if guess < secret:
            print(YELLOW + "too low" + RESET)

        elif guess > secret:
            print(YELLOW + BOLD + "too high" + RESET)
        else:
            print(GREEN + BOLD + "you got it!!!!!! " + "  " + " it took u " + str(tries) + " tries" + RESET)
            return
def menu():
    while True:
        print()
        print(CYAN + BOLD +  "========  game zone  ===========" + RESET)
        print()
        print( RED + "chose the game and tye the degit")
        print()
        print(YELLOW + BOLD + "1" + "  " + RESET + MAGENTA + BOLD + "guess the number" + RESET)
        print()
        print(YELLOW + BOLD + "2" + "  " + RESET + MAGENTA + BOLD + "quit"+ RESET)
        print()
        print(YELLOW + BOLD + "3" + "  " + RESET + MAGENTA + BOLD + "rock paper scirrors" + RESET)
        print()
        print(YELLOW + BOLD + "4" + "  " + RESET + MAGENTA + BOLD + "scrambled words" + RESET)
        print()
        choice = input(GREEN + BOLD + "chose the desired game>  ")

        if choice == "1":
            number_game()
        elif choice == "2":
            print("bye!!!")
            break
        elif  choice == "3":
            rock_game()
        elif choice == "4":
            scramble_game()
        else:
            print("chose a appropite option")

menu()