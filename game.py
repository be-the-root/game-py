
import random

RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

def mansion_game():
    room = "living room"
    inventory = []
    moves = 0

    print()
    print(CYAN + BOLD + "============== escape the mantion ==========" + RESET)
    print()
    print(YELLOW + BOLD + "you wake up in a strange mansion, find the key to escape" + RESET)
    print()

    while True:
        moves = moves + 1


        if room == "living_room":
            print(MAGENTA + BOLD + "------ living room ------" + RESET)
            print()
            print("dusty sofas, broken tv , and a cold fireplace")
            print(BOLD + "exits: " + RESET + "north, south")
            print(BOLD + " you can see : " + RESET + "note, log")
            print()

            cmd = input(GREEN + BOLD + "> " + RESET ).strip().lower()

            if cmd == "north":
                room = "hallway"
            elif cmd == "south":
                if "key" in inventory:
                    print()
                    print(GREEN + BOLD + "you slide the key into the lock----" + RESET)
                    print(GREEN + BOLD + "the door swings open, you escaped!!!" + RESET)
                    print(YELLOW + "you did it in" + str(moves) + " moves" + RESET)
                    print(GREEN + BOLD + " ------ you win ------")
                    return
                else:
                    print(RED + "the front door is locked, u need a key" + RESET)
            elif cmd == "take note":
                if "note" in inventory:
                    print(YELLOW + "you already hvae the note "+ RESET)
                else:
                    inventory.append("note")
                    print(GREEN + "picked up note. it says: 'the key is under the bed" + RESET)
            elif cmd == "take log":
                if "log" in inventory:
                    print(YELLOW + "you already have the log" + RESET)
                else:
                    inventory.append("log")
                    print(GREEN + "picked up the wooden log" + RESET)
            elif cmd == "inventory":
                if len(inventory) == 0:
                    print(YELLOW + "your pokets are empty" + RESET)
                else:
                    print(YELLOW + BOLD + "you have: " + str(inventory) + RESET)
            elif cmd == "quit":
                print(RED + BOLD + "you gave up and now u die, bye!!" + RESET)

                return
            elif cmd == "help":
                print(YELLOW + BOLD + "commands: north south east west up down take search inventory quit")
            else:
                print(RED + "you cant do that here" + RESET)
            print() 


        elif room == "hallway":
            print(MAGENTA + BOLD + "_______hallway______" + RESET)
            print("a long hallway with creepy paintings, the floor creaks")
            print(BOLD + "exits:" + RESET + " north south est west up")
            print("you can see: painting")
            print()

            



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
        print()
        player = input(CYAN + BOLD + "rock (r), paper (p) or scissors (s)>> " + RESET).lower()
        print()
        print()

        if player != "r" and player != "p" and player != "s":
            print(RED + BOLD + "thats not a move" + RESET)


        computer = random.choice(["rock" , "paper" , "scissors"])
        print(MAGENTA + BOLD + "computer picked "+ computer + RESET)
        
        if player == computer:
            print()
            print(YELLOW + BOLD + "tiee" + RESET)
            


        elif player == "r" and computer == "scissors":
            wins = wins + 1
            print()
            print(GREEN + BOLD + "you won!!!!" + RESET)
            


        elif player == "p" and computer == "rock":
            wins =wins + 1
            print()
            print(GREEN + BOLD +  "you won that round" + RESET)
            


        elif player == "s" and computer == "paper":
            wins = wins + 1
            print()
            print(GREEN + BOLD + "you won this round" + RESET)
            


        else:
            losses = losses +1
            print()
            print(RED + BOLD + "you lost this round" + RESET)
        print()   
        print()
        print(GREEN + BOLD + "score : you >> " + str(wins)  + "  -  " + str(losses) + "<< computer" + RESET)

    if wins == 3:
        print(GREEN + BOLD + " you won the match!!!!11" + RESET)
        print()
    else:
        print(RED + BOLD + "computer won , rematch????" + RESET)
        print()          


def number_game():
    secret = random.randint(1 , 100)
    tries = 0

    print()
    print(CYAN + BOLD +  " i picked a number between 1 and 100" + RESET)
    print()


    while True:
        print()
        guess = input(GREEN + BOLD + "ur guess>>>" + RESET)
        print()

        try:
            guess = int(guess)
        except ValueError:
            print(RED + BOLD + "please use a number between 1 to 100" + RESET)
            continue

        tries = tries + 1


        if guess < secret:
            print(YELLOW + BOLD +  "too low" + RESET)
            print()

        elif guess > secret:
            print(YELLOW + BOLD + "too high" + RESET)
            print()
        else:
            print(GREEN + BOLD + "you got it!!!!!! " + "  " + " it took u " + str(tries) + " tries" + RESET)
            return


def menu():
    while True:
        print()
        print(CYAN + BOLD +  "===========  game zone  ===========" + RESET)
        print()
        print( RED + BOLD +  "chose the game and type the degit")
        print()
        print(YELLOW + BOLD + "||  " + "1" + "  " + RESET + MAGENTA + BOLD + "guess the number" + RESET)
        print()
        print(YELLOW + BOLD + "||  " + "2" + "  " + RESET + MAGENTA + BOLD + "quit"+ RESET)
        print()
        print(YELLOW + BOLD + "||  " + "3" + "  " + RESET + MAGENTA + BOLD + "rock paper scirrors" + RESET)
        print()
        print(YELLOW + BOLD + "||  " + "4" + "  " + RESET + MAGENTA + BOLD + "scrambled words" + RESET)
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